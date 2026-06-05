#!/usr/bin/env python3

import argparse
import csv
from collections import Counter


def read_column_values(
    path: str,
    column: int,
    delimiter: str,
    has_header: bool,
) -> list[str]:
    values = []

    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=delimiter)

        if has_header:
            next(reader, None)

        for row_num, row in enumerate(
            reader,
            start=2 if has_header else 1,
        ):
            if column >= len(row):
                raise ValueError(
                    f"Zeile {row_num} in '{path}' hat keine Spalte mit Index {column}"
                )

            values.append(row[column])

    return values


def main():
    parser = argparse.ArgumentParser(
        description="Vergleicht eine Spalte aus zwei CSV-Dateien (Reihenfolge wird ignoriert)."
    )

    parser.add_argument(
        "file1",
        help="Referenzdatei"
    )
    parser.add_argument(
        "file2",
        help="Vergleichsdatei"
    )
    parser.add_argument(
        "column",
        type=int,
        help="0-basierter Spaltenindex"
    )
    parser.add_argument(
        "-d",
        "--delimiter",
        default=",",
        help="CSV-Trennzeichen (Standard: ,)"
    )
    parser.add_argument(
        "--header",
        action="store_true",
        help="Erste Zeile als Header behandeln und überspringen"
    )

    args = parser.parse_args()

    values1 = read_column_values(
        args.file1,
        args.column,
        args.delimiter,
        args.header,
    )

    values2 = read_column_values(
        args.file2,
        args.column,
        args.delimiter,
        args.header,
    )

    counter1 = Counter(values1)
    counter2 = Counter(values2)

    extra_in_file1 = counter1 - counter2
    missing_in_file1 = counter2 - counter1

    if not extra_in_file1 and not missing_in_file1:
        print("✓ Spalten sind identisch.")
        return

    for value, count in sorted(extra_in_file1.items()):
        for _ in range(count):
            print(f'extra:   "{value}" in file {args.file1} extra')

    for value, count in sorted(missing_in_file1.items()):
        for _ in range(count):
            print(f'missing: "{value}" in file {args.file1} missing')


if __name__ == "__main__":
    main()