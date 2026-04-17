#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

# Clean generated site outputs so stale hashed exports do not survive rebuilds.
rm -rf _build/html _build/site

HOST="${HOST:-127.0.0.1}" jupyter-book build --html --force
