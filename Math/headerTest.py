#!/usr/bin/env python3

import argparse
import csv
from glob import glob


def expand_files(patterns: list[str]) -> list[str]:
    files = []
    for pattern in patterns:
        matches = glob(pattern)
        files.extend(matches if matches else [pattern])

    # remove duplicates, keep order
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
        description="Check if all CSV files have identical headers"
    )

    parser.add_argument(
        "files",
        nargs="+",
        help="CSV files or glob patterns",
    )

    parser.add_argument(
        "-d",
        "--delimiter",
        default=",",
        help="CSV delimiter (default: ,)",
    )

    args = parser.parse_args()

    files = expand_files(args.files)

    if len(files) < 2:
        parser.error("Need at least two files.")

    headers = {}

    for path in files:
        headers[path] = read_header(path, args.delimiter)

    reference_file = files[0]
    reference_header = headers[reference_file]

    all_equal = True

    for path in files[1:]:
        if headers[path] == reference_header:
            print(f"✓ {path}")
        else:
            all_equal = False
            print(f"\n=== {path} ===")
            print("❌ Header mismatch")

            ref_set = set(reference_header)
            cur_set = set(headers[path])

            only_in_ref = ref_set - cur_set
            only_in_cur = cur_set - ref_set

            if only_in_ref:
                print(f"Only in {reference_file}:")
                for el in sorted(only_in_ref):
                    print(f"\t{el}")

            if only_in_cur:
                print(f"Only in {path}:")
                for el in sorted(only_in_cur):
                    print(f"\t{el}")

    if all_equal:
        print("✓ All files have identical headers")


if __name__ == "__main__":
    main()