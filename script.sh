#!/bin/bash

# Define base directory (should be the directory containing this script)
if command -v realpath &> /dev/null; then
  BASE_DIR="$(dirname "$(realpath "$0")")"
elif [ -n "$BASH_SOURCE" ]; then
  BASE_DIR="$(dirname "$BASH_SOURCE")"
else
  echo "Could not determine the script directory. Please ensure realpath is installed or use a compatible shell."
  exit 1
fi

# Shortcut function to change to the base directory
function cdr() {
  cd "$BASE_DIR" || { echo "Failed to change to base directory: $BASE_DIR"; return; }
  echo "Current directory: $(pwd)"
}

# Shortcut function to change to the code directory
function cdc() {
  if [ -d "$BASE_DIR/code" ]; then
    cd "$BASE_DIR/code" || { echo "Failed to change to code directory: $BASE_DIR/code"; return; }
    echo "Current directory: $(pwd)"
  else
    echo "Code directory does not exist: $BASE_DIR/code"
  fi
}

# Shortcut function to change to the data directory
function cdd() {
  if [ -d "$BASE_DIR/data" ]; then
    cd "$BASE_DIR/data" || { echo "Failed to change to data directory: $BASE_DIR/data"; return; }
    echo "Current directory: $(pwd)"
  else
    echo "Data directory does not exist: $BASE_DIR/data"
  fi
}

# Shortcut function to change to the font directory
function cdf() {
  if [ -d "$BASE_DIR/font" ]; then
    cd "$BASE_DIR/font" || { echo "Failed to change to font directory: $BASE_DIR/font"; return; }
    echo "Current directory: $(pwd)"
  else
    echo "Font directory does not exist: $BASE_DIR/font"
  fi
}

# Shortcut function to change to the images directory
function cdg() {
  if [ -d "$BASE_DIR/graphics" ]; then
    cd "$BASE_DIR/graphics" || { echo "Failed to change to graphics directory: $BASE_DIR/graphics"; return; }
    echo "Current directory: $(pwd)"
  else
    echo "Graphics directory does not exist: $BASE_DIR/graphics"
  fi
}

# Shortcut function to run the main Python script from the base directory
function run() {
  if [ -f "$BASE_DIR/code/main.py" ]; then
    cdc
    python3 main.py
  else
    echo "main.py not found in code directory: $BASE_DIR/code"
  fi
}

# Function to set up or activate virtual environment
function venv() {
  cdr
  if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install Python3 to continue."
    return
  fi

  if [ -d "venv" ]; then
    # If venv directory exists, check if already activated
    if [ -z "$VIRTUAL_ENV" ]; then
      source venv/bin/activate
    else
      echo "Virtual environment is already activated."
    fi
  else
    # If venv does not exist, create it and install dependencies
    python3 -m venv venv
    source venv/bin/activate
    if ! command -v pip &> /dev/null; then
      echo "pip could not be found. Please ensure pip is installed. You can install pip by running:"
      echo "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py"
      return
    fi
    if [ -f "requirements.txt" ]; then
      pip install -r requirements.txt
    else
      echo "requirements.txt not found. No packages installed."
    fi
  fi
}

