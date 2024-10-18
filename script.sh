#!/bin/bash

# Define base directory (should be the directory containing this script)
BASE_DIR="$(dirname "$(realpath "$0")")"

# Shortcut function to change to the base directory
function cdr() {
    cd "$BASE_DIR" || return
}

# Shortcut function to change to the code directory
function cdc() {
    cd "$BASE_DIR/code" || return
}

# Shortcut function to change to the data directory
function cdd() {
    cd "$BASE_DIR/data" || return
}

# Shortcut function to change to the font directory
function cdf() {
    cd "$BASE_DIR/font" || return
}

# Shortcut function to change to the images directory
function cdg() {
    cd "$BASE_DIR/graphics" || return
}

# Shortcut function to run the main Python script from the base directory
function run() {
    cdc
    python3 main.py
}

