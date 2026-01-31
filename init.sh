#!/bin/bash

# Check if uv is installed (either as standalone or via pip)
if ! command -v uv &> /dev/null && ! python -m uv --version &> /dev/null 2>&1; then
    echo "uv not found. Installing uv via pip..."
    python -m pip install uv
    if [ $? -ne 0 ]; then
        echo "Failed to install uv. Please install it manually:"
        echo "  pip install uv"
        exit 1
    fi
    echo "uv installed successfully!"
fi

# Try uv directly first, fall back to python -m uv if not found
if command -v uv &> /dev/null; then
    uv venv --allow-existing
    uv sync
else
    python -m uv venv --allow-existing
    python -m uv sync
fi

source .venv/bin/activate
python run.py
