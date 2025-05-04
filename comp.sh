#!/bin/zsh

set -e

# Navigate to the script's root directory
cd "$(dirname "$0")"

# Start with the root requirements.in
requirements_files=("requirements.in")
output_files=("requirements.txt")

# Traverse each subdirectory in scripts/
for script_dir in scripts/*; do
  if [ -d "$script_dir" ]; then
    req_file="$script_dir/requirements.in"
    out_file="$script_dir/requirements.txt"
    if [ -f "$req_file" ]; then
      requirements_files+=("$req_file")
      output_files+=("$out_file")
    fi
  fi
done

# Run pip-sync with all collected requirements files
pip-sync "${requirements_files[@]}"

