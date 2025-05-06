#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path
import json
import glob

def list_files_with_extension(extension: str, wildcard: str) -> list:
    """ List files with a certain extension, accept name wildcards.
    Works in the current folder.

    Args:
        extension (str): File extension
        wildcard (str): File name wild card

    Returns:
        list: Resultant list sorted by file name
    """
    current_dir = Path.cwd()  # Get the current working directory as a Path object
    normalized_ext = "." + extension.lower() if not extension.startswith(".") else extension.lower()
    return sorted([
        p.name for p in current_dir.iterdir()
        if p.is_file() and p.suffix.lower() == normalized_ext and p.name in glob.glob(wildcard)
    ])

def parse_args(argv=None):
    """ Parses cli arguments (excluding command) and returns them in a Namespace.

    Args:
        argv (list[str], optional): cli arguments. Defaults to None.

    Returns:
        Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        prog="files2json",
        description="Generate a JSON file from a list of file names with a specific extension.")
    parser.add_argument("-e", "--extension", help="file extension, default: 'jpg'",
                        type=str, default="jpg")
    parser.add_argument("-w", "--wildcard", help="file name wildcard, default: '*'",
                        type=str, default="*")
    parser.add_argument("-j", "--json", help="output json file, default: 'output'",
                        type=str, default="output")
    parser.add_argument("--inspect", action="store_true",
                        help="If set, load and print the JSON file instead of writing")
    return parser.parse_args(argv)

def inspect_json_file(json_path: str):
    """ Inspect (ie. print) json file without overriding.

    Args:
        json_path (str): Path to an existing output json file
    """
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"\nContents of '{json_path}':")
            print(json.dumps(data, indent=2, ensure_ascii=False))
    except FileNotFoundError:
        print(f"Error: File '{json_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{json_path}' is not valid JSON.")

def main():
    """ main program
    """
    args = parse_args(sys.argv[1:])  # Exclude script name from arguments
    json_path = f"{args.json}.json"

    if args.inspect:
        inspect_json_file(json_path)
    else:
        files = list_files_with_extension(args.extension, args.wildcard)
        with open(json_path, "w", encoding="utf-8") as outfile:
            json.dump(files, outfile, ensure_ascii=False, indent=2)
        print(f"Wrote {len(files)} file(s) to {json_path}")

if __name__ == "__main__":
    main()
