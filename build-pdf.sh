#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

pandoc \
  --resource-path=manuscript:. \
  --pdf-engine=xelatex \
  -H style/header.tex \
  --lua-filter=style/subtitle-filter.lua \
  -V geometry:"margin=1in, a4paper" \
  -V fontsize=11pt \
  -V mainfont="DejaVu Serif" \
  -V sansfont="DejaVu Sans" \
  -V monofont="DejaVu Sans Mono" \
  -V documentclass=report \
  --toc \
  --toc-depth=2 \
  --highlight-style=tango \
  --top-level-division=chapter \
  -o manuscript.pdf \
  manuscript/00-preface.md \
  manuscript/01-logistics.md \
  manuscript/02-building-qaoa.md \
  manuscript/03-cryptography.md \
  manuscript/04-inside-shors.md \
  manuscript/05-drug-discovery.md \
  manuscript/06-vqe-pipeline.md \
  manuscript/07-machine-learning.md \
  manuscript/08-quantum-kernels.md \
  manuscript/09-finance.md \
  manuscript/10-amplitude-estimation.md \
  manuscript/11-supply-chains.md \
  manuscript/12-qubo-engineering.md \
  manuscript/13-materials-science.md \
  manuscript/14-qpe-trotter.md \
  manuscript/15-climate-energy.md \
  manuscript/16-quantum-embedding.md

echo "Built manuscript.pdf ($(du -h manuscript.pdf | cut -f1))"
