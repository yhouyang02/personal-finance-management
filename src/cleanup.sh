#!/bin/bash
# Clean up user expense data in csv format
# Usage: ./cleanup.sh

# Define the temp directory path
TEMP_DIR="./temp"

# Check if the temp directory exists
if [ ! -d "$TEMP_DIR" ]; then
    echo "Warning: Temp directory ($TEMP_DIR) does not exist!"
    exit 1
fi

# Check if the temp directory is empty
if [ -z "$(ls -A $TEMP_DIR)" ]; then
    echo "Temp directory is already empty."
    exit 0
fi

# Remove all files and subdirectories in the temp directory
rm -rf "$TEMP_DIR"/*.csv

# Check if the removal was successful
if [ $? -eq 0 ]; then
    echo "Successfully cleaned up temp directory."
else
    echo "Error: Failed to clean up temp directory!"
    exit 1
fi