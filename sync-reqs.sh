#!/bin/zsh

set -e

# Navigate to the script's root directory
cd "$(dirname "$0")"

# Sync root requirements.txt if it exists
if [ -f "requirements.txt" ]; then
  requirements_files=("requirements.txt")
fi

# Traverse each subdirectory in scripts/
for script_dir in scripts/*; do
  if [ -d "$script_dir" ]; then
    req_file="$script_dir/requirements.txt"
    if [ -f "$req_file" ]; then
      requirements_files+=("$req_file")
    fi
  fi
done

# Run pip-sync with all collected requirements files
pip-sync "${requirements_files[@]}"

