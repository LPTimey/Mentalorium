import argparse
import csv
import glob
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

MIN_BIAS = 0.25
A_BIAS = lambda i, r, c: (1 - i) * (((r - 1) / 5) - 1) * (c / 100)
OUTPATH = "out/AutomationBias/"


def load_data(args):
    rows = []

    for pattern in args.files:
        for filename in glob.glob(pattern):

            with open(filename, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=args.delimiter)

                for row in reader:

                    case = next(
                        (row[col] for col in args.case_rows if col in row and row[col]),
                        None,
                    )

                    truth = next(
                        (row[col] for col in args.truth_rows if col in row and row[col]),
                        None,
                    )

                    rating = next(
                        (row[col] for col in args.rating_rows if col in row and row[col]),
                        None,
                    )

                    confidence = next(
                        (
                            row[col]
                            for col in args.confidence_rows
                            if col in row and row[col]
                        ),
                        None,
                    )

                    if (
                        case is None
                        or truth is None
                        or rating is None
                        or confidence is None
                    ):
                        continue

                    try:
                        correct = int(float(truth))
                        rating = int(float(rating))
                        confidence = float(confidence)
                    except ValueError:
                        continue

                    rows.append(
                        {
                            "case": case,
                            "correct": correct,
                            "rating": rating,
                            "confidence": confidence,
                            "bias": A_BIAS(correct, rating, confidence),
                        }
                    )

    return pd.DataFrame(rows)


def plot_histogram(df):
    plt.figure(figsize=(8, 5))
    plt.hist(df["bias"], bins=30)
    plt.xlabel("Automation Bias")
    plt.ylabel("Count")
    plt.title("Bias Distribution")
    plt.tight_layout()
    plt.savefig(f"{OUTPATH}/bias_histogram.png")
    plt.close()


def plot_bias_by_case(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x="case", y="bias")
    plt.xticks(rotation=45, ha="right")
    plt.title("Bias by Case")
    plt.tight_layout()
    plt.savefig(f"{OUTPATH}/bias_by_case_boxplot.png")
    plt.close()


def plot_case_means(df):
    case_mean = (
        df.groupby("case")["bias"]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(12, 6))
    case_mean.plot(kind="bar")
    plt.ylabel("Mean Bias")
    plt.title("Mean Bias per Case")
    plt.tight_layout()
    plt.savefig(f"{OUTPATH}/bias_mean_per_case.png")
    plt.close()


def plot_heatmap(df):
    bins = np.arange(0, 110, 10)

    df = df.copy()
    df["conf_bin"] = pd.cut(df["confidence"], bins=bins)

    pivot = pd.pivot_table(
        df,
        values="bias",
        index="rating",
        columns="conf_bin",
        aggfunc="mean",
    )

    plt.figure(figsize=(10, 5))
    sns.heatmap(
        pivot,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
    )
    plt.title("Mean Bias by Rating and Confidence")
    plt.tight_layout()
    plt.savefig(f"{OUTPATH}/bias_heatmap_rating_confidence.png")
    plt.close()


def plot_confidence_vs_bias(df):
    plt.figure(figsize=(8, 6))
    plt.scatter(
        df["confidence"],
        df["bias"],
        alpha=0.4,
    )
    plt.xlabel("Confidence")
    plt.ylabel("Bias")
    plt.title("Confidence vs Bias")
    plt.tight_layout()
    plt.savefig(f"{OUTPATH}/confidence_vs_bias.png")
    plt.close()


def plot_rating_vs_bias(df):
    plt.figure(figsize=(8, 6))
    plt.scatter(
        df["rating"],
        df["bias"],
        alpha=0.4,
    )
    plt.xlabel("Rating")
    plt.ylabel("Bias")
    plt.title("Rating vs Bias")
    plt.tight_layout()
    plt.savefig(f"{OUTPATH}/rating_vs_bias.png")
    plt.close()


def plot_violin(df):
    plt.figure(figsize=(8, 5))
    sns.violinplot(
        data=df,
        x="rating",
        y="bias",
    )
    plt.title("Bias Distribution by Rating")
    plt.tight_layout()
    plt.savefig(f"{OUTPATH}/bias_violin_rating.png")
    plt.close()


def plot_correctness_per_case(df):
    correctness = (
        df.groupby("case")["correct"]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(12, 6))
    correctness.plot(kind="bar")
    plt.ylabel("Correctness Rate")
    plt.title("Correctness per Case")
    plt.tight_layout()
    plt.savefig(f"{OUTPATH}/correctness_per_case.png")
    plt.close()


def plot_confidence_distribution(df):
    plt.figure(figsize=(8, 5))

    sns.kdeplot(
        data=df[df["correct"] == 1],
        x="confidence",
        label="correct",
    )

    sns.kdeplot(
        data=df[df["correct"] == 0],
        x="confidence",
        label="incorrect",
    )

    plt.legend()
    plt.title("Confidence by Correctness")
    plt.tight_layout()
    plt.savefig(f"{OUTPATH}/confidence_correct_vs_incorrect.png")
    plt.close()


def plot_bias_surface():
    ratings, confidences = np.meshgrid(
        np.arange(1, 6),
        np.arange(0, 101, 5),
    )

    bias = (((ratings - 1) / 5) - 1) * (confidences / 100)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")

    ax.plot_surface(
        ratings,
        confidences,
        bias,
        cmap="viridis",
    )

    ax.set_xlabel("Rating")
    ax.set_ylabel("Confidence")
    ax.set_zlabel("Bias")
    ax.set_title("Automation Bias Surface (incorrect answers only)")

    plt.tight_layout()
    plt.savefig(f"{OUTPATH}/bias_surface.png")
    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description="Automation Bias Analysis"
    )

    parser.add_argument("--files", nargs="+", help="CSV files or glob patterns")
    parser.add_argument("--case_rows", nargs="+", help="row names (multiple) of cases")
    parser.add_argument("--truth_rows", nargs="+", help="row names (multiple) of truth_vals")
    parser.add_argument("--disclaimer_rows", nargs="+", help="row names (multiple) of disclaimer_bool")
    parser.add_argument("--rating_rows", nargs="+", help="row names (multiple) of rating likert")
    parser.add_argument("--confidence_rows", nargs="+", help="row names (multiple) of confidence percent")
    parser.add_argument("-d", "--delimiter", default=",")

    args = parser.parse_args()

    os.makedirs(OUTPATH, exist_ok=True)

    df = load_data(args)

    if df.empty:
        print("No valid rows found.")
        return

    plot_histogram(df)
    plot_bias_by_case(df)
    plot_case_means(df)
    plot_heatmap(df)
    plot_confidence_vs_bias(df)
    plot_rating_vs_bias(df)
    plot_violin(df)
    plot_correctness_per_case(df)
    plot_confidence_distribution(df)
    plot_bias_surface()

    print(f"Generated plots in {OUTPATH}")


if __name__ == "__main__":
    main()