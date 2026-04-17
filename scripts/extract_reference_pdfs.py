from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import os
from pathlib import Path
import re
from typing import Iterable, Sequence

import fitz


CAPTION_START_RE = re.compile(
    r"^(?P<label>(?:Figure|Fig\.?|Table|Scheme|Algorithm|Extended Data Figure|Extended Data Fig\.?|Supplementary Figure|Supplementary Fig\.?)\s+[A-Za-z0-9IVXivx.-]+)",
    re.IGNORECASE,
)

DEFAULT_INPUT_DIR = ".references"
DEFAULT_MARKDOWN_DIR = ".references/markdown"
DEFAULT_FIGURE_REPORT_DIR = ".references/figure-captions"
DEFAULT_FIGURE_OUTPUT_DIR = ".references/figure-crops"

FULL_WIDTH_THRESHOLD = 0.72
COLUMN_MARGIN_RATIO = 0.06
MIN_COLUMN_BLOCKS = 3
MIN_COLUMN_VERTICAL_OVERLAP_RATIO = 0.15
MIN_VISUAL_EDGE = 3.0
MIN_FIGURE_CROP_WIDTH = 40.0
MIN_FIGURE_CROP_HEIGHT = 40.0
FIGURE_PAD = 8.0


@dataclass(frozen=True)
class TextBlock:
    index: int
    rect: fitz.Rect
    text: str


@dataclass(frozen=True)
class ColumnLayout:
    split_x: float
    gutter: float
    left_rect: fitz.Rect
    right_rect: fitz.Rect


@dataclass(frozen=True)
class FigureEntry:
    label: str
    page_number: int
    caption_text: str
    caption_rect: fitz.Rect
    crop_rect: fitz.Rect | None
    image_path: Path | None


@dataclass(frozen=True)
class PageAnalysis:
    text_blocks: list[TextBlock]
    body_blocks: list[TextBlock]
    ordered_blocks: list[TextBlock]
    visual_rects: list[fitz.Rect]
    layout: ColumnLayout | None


@dataclass(frozen=True)
class ExtractionResult:
    pdf_path: Path
    markdown_path: Path | None
    figure_report_path: Path | None
    page_count: int
    title: str | None
    author: str | None
    caption_count: int
    figure_asset_count: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Extract PDFs into analysis-friendly markdown with page boundaries, "
            "column-aware text reflow, and figure-caption sidecars."
        )
    )
    parser.add_argument(
        "inputs",
        nargs="*",
        help=(
            "PDF files or directories to process. Defaults to .references when omitted. "
            "Directories are scanned for PDFs."
        ),
    )
    parser.add_argument(
        "--input-dir",
        action="append",
        default=[],
        help=(
            "Backward-compatible alias for adding an input directory. "
            "May be passed multiple times."
        ),
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Recurse into nested directories when expanding directory inputs.",
    )
    parser.add_argument(
        "--output-dir",
        "--markdown-dir",
        dest="markdown_dir",
        default=DEFAULT_MARKDOWN_DIR,
        help="Directory where extracted markdown files will be written.",
    )
    parser.add_argument(
        "--figure-report-dir",
        default=DEFAULT_FIGURE_REPORT_DIR,
        help="Directory where figure-caption markdown reports will be written.",
    )
    parser.add_argument(
        "--figure-output-dir",
        default=DEFAULT_FIGURE_OUTPUT_DIR,
        help="Directory where extracted figure crops will be written.",
    )
    parser.add_argument(
        "--skip-markdown",
        action="store_true",
        help="Skip text-markdown extraction and only produce figure-caption outputs.",
    )
    parser.add_argument(
        "--skip-figures",
        action="store_true",
        help="Skip figure-caption extraction and only produce text-markdown outputs.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing outputs.",
    )
    return parser.parse_args()


def clean_block_text(text: str) -> str:
    text = text.replace("\x00", "")
    text = text.replace("\u00a0", " ")
    lines = [re.sub(r"[ \t]{2,}", " ", line.strip()) for line in text.splitlines()]
    stripped_lines = [line for line in lines if line]
    if not stripped_lines:
        return ""
    return "\n".join(stripped_lines).strip()


def relative_path(from_dir: Path, to_path: Path) -> Path:
    return Path(os.path.relpath(to_path, from_dir))


def rect_area(rect: fitz.Rect) -> float:
    return max(0.0, rect.width) * max(0.0, rect.height)


def intersection_area(left: fitz.Rect, right: fitz.Rect) -> float:
    x0 = max(left.x0, right.x0)
    y0 = max(left.y0, right.y0)
    x1 = min(left.x1, right.x1)
    y1 = min(left.y1, right.y1)
    if x1 <= x0 or y1 <= y0:
        return 0.0
    return (x1 - x0) * (y1 - y0)


def horizontal_overlap(left: fitz.Rect, right: fitz.Rect) -> float:
    return max(0.0, min(left.x1, right.x1) - max(left.x0, right.x0))


def union_rect(left: fitz.Rect, right: fitz.Rect) -> fitz.Rect:
    return fitz.Rect(
        min(left.x0, right.x0),
        min(left.y0, right.y0),
        max(left.x1, right.x1),
        max(left.y1, right.y1),
    )


def expand_rect(rect: fitz.Rect, pad: float, page_rect: fitz.Rect | None = None) -> fitz.Rect:
    expanded = fitz.Rect(rect.x0 - pad, rect.y0 - pad, rect.x1 + pad, rect.y1 + pad)
    if page_rect is None:
        return expanded
    return fitz.Rect(
        max(page_rect.x0, expanded.x0),
        max(page_rect.y0, expanded.y0),
        min(page_rect.x1, expanded.x1),
        min(page_rect.y1, expanded.y1),
    )


def dedupe_rects(rects: Iterable[fitz.Rect]) -> list[fitz.Rect]:
    unique: list[fitz.Rect] = []
    seen: set[tuple[float, float, float, float]] = set()
    for rect in rects:
        key = tuple(round(value, 1) for value in (rect.x0, rect.y0, rect.x1, rect.y1))
        if key in seen:
            continue
        seen.add(key)
        unique.append(rect)
    return unique


def merge_rects(rects: Sequence[fitz.Rect], page_rect: fitz.Rect, pad: float = 6.0) -> list[fitz.Rect]:
    merged: list[fitz.Rect] = []
    for rect in sorted(rects, key=lambda item: (item.y0, item.x0, item.y1, item.x1)):
        current = fitz.Rect(rect)
        index = 0
        while index < len(merged):
            existing = merged[index]
            if expand_rect(existing, pad, page_rect).intersects(expand_rect(current, pad, page_rect)):
                current = union_rect(existing, current)
                merged.pop(index)
                index = 0
                continue
            index += 1
        merged.append(current)
    return merged


def title_quote(text: str) -> str:
    return text.replace('"', "'")


def block_text(block: dict) -> str:
    line_texts: list[str] = []
    for line in block.get("lines", []):
        spans = "".join(span.get("text", "") for span in line.get("spans", []))
        cleaned = clean_block_text(spans)
        if cleaned:
            line_texts.append(cleaned)
    if line_texts:
        return "\n".join(line_texts)
    return clean_block_text(block.get("text", ""))


def extract_text_blocks(page: fitz.Page) -> list[TextBlock]:
    blocks: list[TextBlock] = []
    for index, block in enumerate(page.get_text("dict")["blocks"]):
        if block.get("type") != 0:
            continue
        text = block_text(block)
        if not text:
            continue
        blocks.append(TextBlock(index=index, rect=fitz.Rect(block["bbox"]), text=text))
    return blocks


def extract_visual_rects(page: fitz.Page) -> list[fitz.Rect]:
    page_rect = page.rect
    rects: list[fitz.Rect] = []

    for block in page.get_text("dict")["blocks"]:
        if block.get("type") != 1:
            continue
        rect = fitz.Rect(block["bbox"])
        if max(rect.width, rect.height) >= MIN_VISUAL_EDGE:
            rects.append(rect)

    for image in page.get_images(full=True):
        for rect in page.get_image_rects(image[0]):
            if max(rect.width, rect.height) >= MIN_VISUAL_EDGE:
                rects.append(fitz.Rect(rect))

    for drawing in page.get_drawings():
        drawing_rect = drawing.get("rect")
        if drawing_rect is None:
            continue
        rect = fitz.Rect(drawing_rect)
        if max(rect.width, rect.height) >= MIN_VISUAL_EDGE:
            rects.append(rect)

    return merge_rects(dedupe_rects(rects), page_rect)


def is_caption_block(text: str) -> bool:
    first_line = text.splitlines()[0].strip() if text.splitlines() else ""
    return bool(CAPTION_START_RE.match(first_line))


def caption_label(text: str) -> str:
    first_line = text.splitlines()[0].strip() if text.splitlines() else ""
    match = CAPTION_START_RE.match(first_line)
    if not match:
        return "Figure"
    return match.group("label")


def is_marginalia_block(block: TextBlock, page_rect: fitz.Rect) -> bool:
    text = block.text.strip()
    if not text:
        return True
    short_single_line = "\n" not in text and len(text) <= 6
    top_band = page_rect.y0 + page_rect.height * 0.06
    bottom_band = page_rect.y1 - page_rect.height * 0.05
    if short_single_line and (block.rect.y1 <= top_band or block.rect.y0 >= bottom_band):
        return True
    return False


def overlap_ratio(block_rect: fitz.Rect, visual_rects: Sequence[fitz.Rect]) -> float:
    area = rect_area(block_rect)
    if area <= 0:
        return 0.0
    best = 0.0
    for rect in visual_rects:
        best = max(best, intersection_area(block_rect, rect) / area)
    return best


def is_visual_text(block: TextBlock, visual_rects: Sequence[fitz.Rect]) -> bool:
    if is_caption_block(block.text):
        return False
    ratio = overlap_ratio(block.rect, visual_rects)
    word_count = len(block.text.split())
    if ratio >= 0.85:
        return True
    if ratio >= 0.6 and word_count <= 40:
        return True
    return False


def detect_column_layout(blocks: Sequence[TextBlock], page_rect: fitz.Rect) -> ColumnLayout | None:
    if len(blocks) < 6:
        return None

    split_x = page_rect.x0 + page_rect.width / 2
    gutter = page_rect.width * COLUMN_MARGIN_RATIO
    narrow_blocks = [block for block in blocks if block.rect.width < page_rect.width * FULL_WIDTH_THRESHOLD]
    left = [block for block in narrow_blocks if block.rect.x1 <= split_x + gutter]
    right = [block for block in narrow_blocks if block.rect.x0 >= split_x - gutter]
    if len(left) < MIN_COLUMN_BLOCKS or len(right) < MIN_COLUMN_BLOCKS:
        return None

    left_y = (min(block.rect.y0 for block in left), max(block.rect.y1 for block in left))
    right_y = (min(block.rect.y0 for block in right), max(block.rect.y1 for block in right))
    overlap = min(left_y[1], right_y[1]) - max(left_y[0], right_y[0])
    if overlap < page_rect.height * MIN_COLUMN_VERTICAL_OVERLAP_RATIO:
        return None

    left_rect = fitz.Rect(
        min(block.rect.x0 for block in left),
        page_rect.y0,
        max(block.rect.x1 for block in left),
        page_rect.y1,
    )
    right_rect = fitz.Rect(
        min(block.rect.x0 for block in right),
        page_rect.y0,
        max(block.rect.x1 for block in right),
        page_rect.y1,
    )
    return ColumnLayout(split_x=split_x, gutter=gutter, left_rect=left_rect, right_rect=right_rect)


def block_role(block: TextBlock, layout: ColumnLayout | None, page_rect: fitz.Rect) -> str:
    if layout is None:
        return "span"
    if block.rect.width >= page_rect.width * FULL_WIDTH_THRESHOLD:
        return "span"
    if block.rect.x1 <= layout.split_x + layout.gutter:
        return "left"
    if block.rect.x0 >= layout.split_x - layout.gutter:
        return "right"
    return "span"


def block_sort_key(block: TextBlock) -> tuple[float, float, int]:
    return (round(block.rect.y0, 2), round(block.rect.x0, 2), block.index)


def order_blocks(blocks: Sequence[TextBlock], page_rect: fitz.Rect) -> tuple[list[TextBlock], ColumnLayout | None]:
    ordered_by_position = sorted(blocks, key=block_sort_key)
    layout = detect_column_layout(blocks, page_rect)
    if layout is None:
        return ordered_by_position, None

    ordered: list[TextBlock] = []
    pending_columns: list[TextBlock] = []

    def flush_pending() -> None:
        nonlocal pending_columns
        if not pending_columns:
            return
        left = sorted(
            [block for block in pending_columns if block_role(block, layout, page_rect) == "left"],
            key=block_sort_key,
        )
        right = sorted(
            [block for block in pending_columns if block_role(block, layout, page_rect) == "right"],
            key=block_sort_key,
        )
        spans = sorted(
            [block for block in pending_columns if block_role(block, layout, page_rect) == "span"],
            key=block_sort_key,
        )
        ordered.extend(left)
        ordered.extend(right)
        ordered.extend(spans)
        pending_columns = []

    for block in ordered_by_position:
        role = block_role(block, layout, page_rect)
        if role == "span":
            flush_pending()
            ordered.append(block)
        else:
            pending_columns.append(block)

    flush_pending()
    return ordered, layout


def analyze_page(page: fitz.Page) -> PageAnalysis:
    text_blocks = extract_text_blocks(page)
    visual_rects = extract_visual_rects(page)
    body_blocks = [
        block
        for block in text_blocks
        if not is_marginalia_block(block, page.rect) and not is_visual_text(block, visual_rects)
    ]
    ordered_blocks, layout = order_blocks(body_blocks, page.rect)
    return PageAnalysis(
        text_blocks=text_blocks,
        body_blocks=body_blocks,
        ordered_blocks=ordered_blocks,
        visual_rects=visual_rects,
        layout=layout,
    )


def page_to_markdown(analysis: PageAnalysis) -> str:
    if not analysis.ordered_blocks:
        return ""
    return "\n\n".join(block.text for block in analysis.ordered_blocks).strip()


def column_region_for_caption(
    caption_rect: fitz.Rect,
    layout: ColumnLayout | None,
    page_rect: fitz.Rect,
) -> fitz.Rect:
    if layout is None or caption_rect.width >= page_rect.width * FULL_WIDTH_THRESHOLD:
        return fitz.Rect(page_rect)

    center_x = (caption_rect.x0 + caption_rect.x1) / 2
    if center_x <= layout.split_x:
        return fitz.Rect(layout.left_rect)
    return fitz.Rect(layout.right_rect)


def crop_rect_for_caption(
    caption_block: TextBlock,
    analysis: PageAnalysis,
    page_rect: fitz.Rect,
) -> fitz.Rect | None:
    region = column_region_for_caption(caption_block.rect, analysis.layout, page_rect)
    caption_top = caption_block.rect.y0
    full_width_caption = caption_block.rect.width >= page_rect.width * FULL_WIDTH_THRESHOLD

    prior_blocks = [
        block
        for block in analysis.body_blocks
        if block.index != caption_block.index
        and block.rect.y1 <= caption_top
        and horizontal_overlap(block.rect, region) > 0
    ]
    fallback_top = page_rect.y0 + FIGURE_PAD
    if prior_blocks:
        fallback_top = max(block.rect.y1 for block in prior_blocks) + FIGURE_PAD
    fallback = fitz.Rect(region.x0, fallback_top, region.x1, caption_top - 4.0)
    fallback_valid = (
        fallback.width >= MIN_FIGURE_CROP_WIDTH and fallback.height >= MIN_FIGURE_CROP_HEIGHT
    )
    page_band_fallback = fitz.Rect(
        page_rect.x0 + FIGURE_PAD,
        page_rect.y0 + FIGURE_PAD,
        page_rect.x1 - FIGURE_PAD,
        caption_top - 4.0,
    )
    page_band_valid = (
        page_band_fallback.width >= MIN_FIGURE_CROP_WIDTH
        and page_band_fallback.height >= MIN_FIGURE_CROP_HEIGHT
    )

    candidates: list[fitz.Rect] = []
    for rect in analysis.visual_rects:
        if rect.y1 >= caption_top - 1:
            continue
        if horizontal_overlap(rect, region) <= 0:
            continue
        candidates.append(rect)

    if candidates:
        crop = merge_rects(candidates, page_rect, pad=FIGURE_PAD)
        union = crop[0]
        for rect in crop[1:]:
            union = union_rect(union, rect)
        clipped = fitz.Rect(
            max(region.x0, union.x0 - FIGURE_PAD),
            max(page_rect.y0, union.y0 - FIGURE_PAD),
            min(region.x1, union.x1 + FIGURE_PAD),
            min(caption_top - 4.0, union.y1 + FIGURE_PAD),
        )
        if clipped.width >= MIN_FIGURE_CROP_WIDTH and clipped.height >= MIN_FIGURE_CROP_HEIGHT:
            if full_width_caption and page_band_valid and clipped.width < region.width * 0.7:
                return page_band_fallback
            if fallback_valid and clipped.width < fallback.width * 0.55:
                return fallback
            return clipped

    if full_width_caption and page_band_valid:
        return page_band_fallback
    if fallback_valid:
        return fallback
    return None


def save_crop(page: fitz.Page, crop_rect: fitz.Rect, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=crop_rect, alpha=False)
    pixmap.save(output_path)


def extract_figure_entries(
    page: fitz.Page,
    analysis: PageAnalysis,
    pdf_stem: str,
    figure_output_dir: Path,
) -> list[FigureEntry]:
    caption_blocks = [block for block in analysis.body_blocks if is_caption_block(block.text)]
    entries: list[FigureEntry] = []
    for index, caption_block in enumerate(caption_blocks, start=1):
        crop_rect = crop_rect_for_caption(caption_block, analysis, page.rect)
        image_path: Path | None = None
        if crop_rect is not None:
            image_path = figure_output_dir / pdf_stem / f"page_{page.number + 1:03d}_figure_{index:02d}.png"
            save_crop(page, crop_rect, image_path)
        entries.append(
            FigureEntry(
                label=caption_label(caption_block.text),
                page_number=page.number + 1,
                caption_text=caption_block.text,
                caption_rect=caption_block.rect,
                crop_rect=crop_rect,
                image_path=image_path,
            )
        )
    return entries


def build_markdown_lines(
    pdf_path: Path,
    page_count: int,
    title: str | None,
    author: str | None,
    page_contents: Sequence[str],
    extracted_at: str,
) -> list[str]:
    relative_pdf = Path("..") / pdf_path.name
    lines: list[str] = [
        "---",
        f"source_pdf: {relative_pdf.as_posix()}",
        f"pages: {page_count}",
        f"extracted_at: {extracted_at}",
        "extractor: PyMuPDF (fitz)",
        "reflow: column-aware block ordering",
    ]
    if title:
        lines.append(f'title: "{title_quote(title)}"')
    if author:
        lines.append(f'author: "{title_quote(author)}"')
    lines.extend(["---", "", f"# {pdf_path.stem}", ""])
    if title:
        lines.append(f"Original title: {title}")
        lines.append("")
    if author:
        lines.append(f"Author metadata: {author}")
        lines.append("")
    lines.append(f"Source PDF: {relative_pdf.as_posix()}")
    lines.append("")
    lines.append(
        "> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade."
    )
    lines.append("")

    for page_number, content in enumerate(page_contents, start=1):
        lines.append(f"## Page {page_number}")
        lines.append("")
        lines.append(content if content else "_No extractable text found on this page._")
        lines.append("")

    return lines


def build_figure_report_lines(
    pdf_path: Path,
    page_count: int,
    title: str | None,
    author: str | None,
    entries: Sequence[FigureEntry],
    report_path: Path,
    extracted_at: str,
) -> list[str]:
    relative_pdf = Path("..") / pdf_path.name
    lines: list[str] = [
        "---",
        f"source_pdf: {relative_pdf.as_posix()}",
        f"pages: {page_count}",
        f"captions: {len(entries)}",
        f"extracted_at: {extracted_at}",
        "extractor: PyMuPDF (fitz)",
    ]
    if title:
        lines.append(f'title: "{title_quote(title)}"')
    if author:
        lines.append(f'author: "{title_quote(author)}"')
    lines.extend(["---", "", f"# {pdf_path.stem} Figure Report", ""])

    if not entries:
        lines.append("No figure or table captions detected.")
        lines.append("")
        return lines

    lines.append(
        "This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually."
    )
    lines.append("")

    for entry in entries:
        lines.append(f"## {entry.label}")
        lines.append("")
        lines.append(f"Page: {entry.page_number}")
        lines.append(
            "Caption bbox: "
            f"({entry.caption_rect.x0:.1f}, {entry.caption_rect.y0:.1f}, {entry.caption_rect.x1:.1f}, {entry.caption_rect.y1:.1f})"
        )
        if entry.crop_rect is not None:
            lines.append(
                "Crop bbox: "
                f"({entry.crop_rect.x0:.1f}, {entry.crop_rect.y0:.1f}, {entry.crop_rect.x1:.1f}, {entry.crop_rect.y1:.1f})"
            )
        if entry.image_path is not None:
            rel_image = relative_path(report_path.parent, entry.image_path)
            lines.append(f"Crop asset: {rel_image.as_posix()}")
        else:
            lines.append("Crop asset: none")
        lines.append("")
        lines.append("Caption:")
        lines.append("")
        lines.append(entry.caption_text)
        lines.append("")

    return lines


def extract_pdf(
    pdf_path: Path,
    markdown_dir: Path,
    figure_report_dir: Path,
    figure_output_dir: Path,
    skip_markdown: bool,
    skip_figures: bool,
) -> ExtractionResult:
    with fitz.open(pdf_path) as document:
        metadata = document.metadata or {}
        title = metadata.get("title") or None
        author = metadata.get("author") or None
        page_count = document.page_count
        extracted_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

        page_contents: list[str] = []
        figure_entries: list[FigureEntry] = []
        for page_number in range(page_count):
            page = document.load_page(page_number)
            analysis = analyze_page(page)
            if not skip_markdown:
                page_contents.append(page_to_markdown(analysis))
            if not skip_figures:
                figure_entries.extend(
                    extract_figure_entries(page, analysis, pdf_path.stem, figure_output_dir)
                )

    markdown_path: Path | None = None
    if not skip_markdown:
        markdown_dir.mkdir(parents=True, exist_ok=True)
        markdown_path = markdown_dir / f"{pdf_path.stem}.md"
        markdown_lines = build_markdown_lines(
            pdf_path=pdf_path,
            page_count=page_count,
            title=title,
            author=author,
            page_contents=page_contents,
            extracted_at=extracted_at,
        )
        markdown_path.write_text("\n".join(markdown_lines).rstrip() + "\n")

    figure_report_path: Path | None = None
    if not skip_figures:
        figure_report_dir.mkdir(parents=True, exist_ok=True)
        figure_report_path = figure_report_dir / f"{pdf_path.stem}.md"
        report_lines = build_figure_report_lines(
            pdf_path=pdf_path,
            page_count=page_count,
            title=title,
            author=author,
            entries=figure_entries,
            report_path=figure_report_path,
            extracted_at=extracted_at,
        )
        figure_report_path.write_text("\n".join(report_lines).rstrip() + "\n")

    return ExtractionResult(
        pdf_path=pdf_path,
        markdown_path=markdown_path,
        figure_report_path=figure_report_path,
        page_count=page_count,
        title=title,
        author=author,
        caption_count=len(figure_entries),
        figure_asset_count=sum(1 for entry in figure_entries if entry.image_path is not None),
    )


def build_markdown_index(results: Iterable[ExtractionResult], output_dir: Path) -> None:
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    lines = [
        "# Reference Markdown Index",
        "",
        f"Generated: {timestamp}",
        "",
        "This directory contains page-delimited markdown extractions of PDFs processed by the archive extractor.",
        "",
        "| PDF | Markdown | Pages | Figure report | Captions | Crops |",
        "|---|---|---:|---|---:|---:|",
    ]
    for result in sorted(results, key=lambda item: item.pdf_path.name):
        markdown_name = result.markdown_path.name if result.markdown_path is not None else "-"
        figure_name = (
            result.figure_report_path.name if result.figure_report_path is not None else "-"
        )
        lines.append(
            f"| {result.pdf_path.name} | {markdown_name} | {result.page_count} | {figure_name} | {result.caption_count} | {result.figure_asset_count} |"
        )
    lines.append("")
    (output_dir / "INDEX.md").write_text("\n".join(lines))


def build_figure_index(results: Iterable[ExtractionResult], figure_report_dir: Path) -> None:
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    lines = [
        "# Figure Report Index",
        "",
        f"Generated: {timestamp}",
        "",
        "This directory contains caption reports for PDFs processed by the archive extractor.",
        "",
        "| PDF | Report | Captions | Crops |",
        "|---|---|---:|---:|",
    ]
    for result in sorted(results, key=lambda item: item.pdf_path.name):
        report_name = result.figure_report_path.name if result.figure_report_path is not None else "-"
        lines.append(
            f"| {result.pdf_path.name} | {report_name} | {result.caption_count} | {result.figure_asset_count} |"
        )
    lines.append("")
    (figure_report_dir / "INDEX.md").write_text("\n".join(lines))


def resolve_pdf_paths(inputs: Sequence[str], input_dirs: Sequence[str], recursive: bool) -> list[Path]:
    requested = list(inputs) + list(input_dirs)
    if not requested:
        requested = [DEFAULT_INPUT_DIR]

    pdf_paths: set[Path] = set()
    for raw_path in requested:
        path = Path(raw_path).resolve()
        if path.is_file():
            if path.suffix.lower() != ".pdf":
                raise SystemExit(f"Not a PDF: {path}")
            pdf_paths.add(path)
            continue
        if path.is_dir():
            pattern = "**/*.pdf" if recursive else "*.pdf"
            for pdf_path in path.glob(pattern):
                if pdf_path.is_file():
                    pdf_paths.add(pdf_path.resolve())
            continue
        raise SystemExit(f"Input path does not exist: {path}")

    return sorted(pdf_paths)


def main() -> None:
    args = parse_args()
    if args.skip_markdown and args.skip_figures:
        raise SystemExit("Nothing to do: both --skip-markdown and --skip-figures were set.")

    pdf_paths = resolve_pdf_paths(args.inputs, args.input_dir, args.recursive)
    if not pdf_paths:
        raise SystemExit("No PDFs found in the requested inputs.")

    markdown_dir = Path(args.markdown_dir).resolve()
    figure_report_dir = Path(args.figure_report_dir).resolve()
    figure_output_dir = Path(args.figure_output_dir).resolve()

    results: list[ExtractionResult] = []
    for pdf_path in pdf_paths:
        results.append(
            extract_pdf(
                pdf_path=pdf_path,
                markdown_dir=markdown_dir,
                figure_report_dir=figure_report_dir,
                figure_output_dir=figure_output_dir,
                skip_markdown=args.skip_markdown,
                skip_figures=args.skip_figures,
            )
        )

    if not args.skip_markdown:
        build_markdown_index(results, markdown_dir)
    if not args.skip_figures:
        build_figure_index(results, figure_report_dir)

    summary = [f"Processed {len(results)} PDFs"]
    if not args.skip_markdown:
        summary.append(f"markdown: {markdown_dir}")
    if not args.skip_figures:
        summary.append(f"figure reports: {figure_report_dir}")
        summary.append(f"figure crops: {figure_output_dir}")
    print(" | ".join(summary))


if __name__ == "__main__":
    main()
