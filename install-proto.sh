#!/bin/bash

source_file="hashtool.py"
destination_directory="$HOME/.Kitware/HashTool"
mkdir -p "$destination_directory"
cp "$source_file" "$destination_directory"
chmod +x "$destination_directory/$source_file"
echo "The file $source_file has been copied to $destination_directory, and execution permissions have been granted."
