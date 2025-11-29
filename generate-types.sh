#!/bin/bash

# This script generates TypeScript types from Pydantic models.

# Exit on error
set -e

# Project root
ROOT_DIR=$(git rev-parse --show-toplevel)
VENV_BIN="$ROOT_DIR/.venv/bin"
BACKEND_MODELS_FILE="$ROOT_DIR/backend/models.py"
TYPESCRIPT_OUTPUT_DIR="$ROOT_DIR/extension/types"
TYPESCRIPT_OUTPUT_FILE="$TYPESCRIPT_OUTPUT_DIR/models.ts"

# Check if json-schema-to-typescript is installed
if ! [ -f "$ROOT_DIR/extension/node_modules/.bin/json2ts" ]; then
    echo "json-schema-to-typescript not found. Installing..."
    (cd "$ROOT_DIR/extension" && npm install --save-dev json-schema-to-typescript)
fi

# Install pydantic-to-typescript if not installed
if ! "$VENV_BIN/pip" show pydantic-to-typescript > /dev/null; then
    echo "pydantic-to-typescript not found. Installing..."
    "$VENV_BIN/pip" install pydantic-to-typescript
fi

# Create output directory if it doesn't exist
mkdir -p "$TYPESCRIPT_OUTPUT_DIR"

# Generate TypeScript types
echo "Generating TypeScript types from Pydantic models..."
PYTHONPATH="$ROOT_DIR" PATH="$ROOT_DIR/extension/node_modules/.bin:$PATH" "$VENV_BIN/pydantic2ts" --module backend.models --output "$TYPESCRIPT_OUTPUT_FILE"

echo "TypeScript types generated successfully at $TYPESCRIPT_OUTPUT_FILE"