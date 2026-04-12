-- Pandoc Lua filter:
-- 1. Split chapter titles at " — " into title + gray italic subtitle
-- 2. Inject chapter ink colour BEFORE the heading (so TOC stays clean)

function Header(el)
  if el.level ~= 1 then return nil end

  -- Track chapter count: odd = Unit (purple), even = Deep-Dive (green)
  if not _chapter_count then _chapter_count = 0 end
  _chapter_count = _chapter_count + 1
  local is_unit = (_chapter_count % 2 == 1)
  local ink = is_unit and "darkpurple" or "deepgreen"

  -- Set colour BEFORE the heading — applies to heading text on the page
  -- but does NOT pollute the .toc file with colour commands
  local color_before = pandoc.RawBlock("latex", "\\color{" .. ink .. "}")

  -- Walk inlines to find em dash
  local inlines = el.content
  local split_pos = nil
  for i, inline in ipairs(inlines) do
    if inline.t == "Str" and inline.text:find("\u{2014}") then
      split_pos = i
      break
    end
  end

  -- No subtitle (deep-dives): plain title, colour set before
  if not split_pos then
    return {color_before, el}
  end

  -- Build title (before em dash) — plain text, no colour wrapping
  local title_inlines = {}
  for i = 1, split_pos - 1 do
    table.insert(title_inlines, inlines[i])
  end
  while #title_inlines > 0 and title_inlines[#title_inlines].t == "Space" do
    table.remove(title_inlines)
  end

  -- Build subtitle (after em dash), stripping Emph wrappers
  local sub_inlines = {}
  local remainder = inlines[split_pos].text:match("\u{2014}%s*(.*)")
  if remainder and remainder ~= "" then
    table.insert(sub_inlines, pandoc.Str(remainder))
  end
  for i = split_pos + 1, #inlines do
    local item = inlines[i]
    if item.t == "Emph" then
      for _, child in ipairs(item.content) do
        table.insert(sub_inlines, child)
      end
    else
      table.insert(sub_inlines, item)
    end
  end
  while #sub_inlines > 0 and sub_inlines[1].t == "Space" do
    table.remove(sub_inlines, 1)
  end

  -- Render subtitle as gray italic via raw LaTeX
  local sub_text = pandoc.utils.stringify(pandoc.Inlines(sub_inlines))
  sub_text = sub_text:gsub("\\", "\\textbackslash{}")
  sub_text = sub_text:gsub("%%", "\\%%")
  sub_text = sub_text:gsub("%$", "\\$")
  sub_text = sub_text:gsub("&", "\\&")
  sub_text = sub_text:gsub("#", "\\#")
  sub_text = sub_text:gsub("_", "\\_")
  local subtitle_block = pandoc.RawBlock("latex",
    "\\vspace{-8pt}\\begin{center}{\\large\\itshape\\color{gray}" ..
    sub_text ..
    "}\\end{center}\\vspace{4pt}")

  return {color_before, pandoc.Header(1, title_inlines), subtitle_block}
end
