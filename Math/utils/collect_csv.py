import csv
import os
from enum import IntEnum
from glob import glob
import argparse

session1_files = glob("data/session 1/*.csv")
session2_files = glob("data/session 2/*.csv")

TO_HEADERS = (
    "Nickname",
    "Bias Mean",
    "Bias 1",
    "Bias 2",
    "Bias 3",
    "Group",
    "Session",
    "Vignette 1",
    "Integrity 1",
    "Rating 1",
    "Confidence 1",
    "Vignette 2",
    "Integrity 2",
    "Rating 2",
    "Confidence 2",
    "Vignette 3",
    "Integrity 3",
    "Rating 3",
    "Confidence 3",
    "Age",
    "Gender",
    "AI Useful (allg.)",
    "AI Useful (mental)",
    "AI Acceptability (allg.)",
    "AI Acceptability (mental)",
)

def collect_into(path:str):
    pass

def main():
    parser = parser = argparse.ArgumentParser(
        description="Vergleicht eine Spalte aus zwei CSV-Dateien (Reihenfolge wird ignoriert)."
    )

    parser.add_argument("out_path", help="output path")
    args = parser.parse_args()
    collect_into(args.out_path)


if __name__ == "__main__":
    main()
