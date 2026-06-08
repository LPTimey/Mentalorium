#!/usr/bin/env python3

import argparse
import csv
from glob import glob
from collections import defaultdict


def expand_files(patterns: list[str]) -> list[str]:
    files = []
    for pattern in patterns:
        matches = glob(pattern)
        files.extend(matches if matches else [pattern])

    seen = set()
    result = []
    for f in files:
        if f not in seen:
            seen.add(f)
            result.append(f)
    return result


def read_header(path: str, delimiter: str) -> list[str]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=delimiter)
        return next(reader, [])


def main():
    parser = argparse.ArgumentParser(
        description="Compare CSV headers across multiple files"
    )

    parser.add_argument("files", nargs="+", help="CSV files or glob patterns")
    parser.add_argument("-d", "--delimiter", default=",")

    args = parser.parse_args()

    files = expand_files(args.files)

    if len(files) < 2:
        parser.error("Need at least two files.")

    headers = {f: read_header(f, args.delimiter) for f in files}

    max_len = max(len(h) for h in headers.values())

    all_equal = True

    for i in range(max_len):
        value_map = defaultdict(list)

        for f in files:
            h = headers[f]
            val = h[i] if i < len(h) else "<MISSING>"
            value_map[val].append(f)

        if len(value_map) <= 1:
            continue

        all_equal = False

        spellings = list(value_map.keys())

        print(f"position {i}:")

        for idx, spelling in enumerate(spellings, start=1):
            print(f"{idx}: {spelling}")

        print("in:")
        for idx, file_list in enumerate(value_map.values(), start=1):
            for path in file_list:
                print(f"{idx}: {path}")

        print()

    if all_equal:
        print("✓ All files have identical headers")


if __name__ == "__main__":
    main()