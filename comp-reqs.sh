#!/usr/bin/env zsh
set -e

# Navigate to the script's root directory
cd "$(dirname "$0")"

# Compile root requirements.in if it exists
if [ -f "requirements.in" ]; then
  pip-compile requirements.in --output-file requirements.txt
fi

# Traverse scripts/* directories
for script_dir in scripts/*; do
  if [ -d "$script_dir" ]; then
    input_file="$script_dir/requirements.in"
    output_file="$script_dir/requirements.txt"
    if [ -f "$input_file" ]; then
      pip-compile "$input_file" --output-file "$output_file"
    fi
  fi
done
