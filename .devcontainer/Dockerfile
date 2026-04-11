# ============================================================================
# Problem Down — Book Development Container
# ============================================================================
# Python + Jupyter + Qiskit (circuit drawing) + LaTeX (quantikz, PDF export)
# + Jupyter Book (publishing) + plotting tools
# ============================================================================

FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm

ENV DEBIAN_FRONTEND=noninteractive

# LaTeX (for quantikz circuit diagrams and Jupyter Book PDF export)
RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-pictures \
    texlive-science \
    texlive-xetex \
    lmodern \
    latexmk \
    pandoc \
    make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
