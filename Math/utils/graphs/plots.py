import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import seaborn as sns
from utils import parse_bool


def mental_usefulness(
    df: pd.DataFrame,
    out_path: str,
    formats: list[str] = ["png"],
    display: bool = False,
):
    dataframe = df.copy()

    # identify usefulness columns across sessions
    usefulness_cols = [
        col for col in dataframe.columns if col.startswith("usefulness (mental health)")
    ]

    if not usefulness_cols:
        raise ValueError("No usefulness (mental health) columns found.")

    # convert to numeric and compute per-person mean
    dataframe[usefulness_cols] = dataframe[usefulness_cols].apply(
        pd.to_numeric, errors="coerce"
    )
    dataframe["mean_usefulness"] = dataframe[usefulness_cols].mean(axis=1)

    # ensure bias score exists (fallback safety)
    if "mean_bias_score" not in dataframe.columns:
        raise ValueError("mean_bias_score column missing in dataframe.")

    plt.figure(figsize=(7, 5))

    sns.boxplot(
        data=dataframe,
        x=pd.cut(dataframe["mean_usefulness"], bins=5),
        y="mean_bias_score",
    )

    plt.title("Rated Usefulness of AI in Mental Health vs mean Automation Bias")
    plt.xlabel("Mean rated Mental Health Usefulness (binned)")
    plt.ylabel("Mean Automation Bias")

    plt.tight_layout()

    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    for fmt in formats:
        plt.savefig(f"{out_path}.{fmt}", dpi=300, bbox_inches="tight")

    if display:
        plt.show()

    plt.close()


def groups(
    plot,
    df: pd.DataFrame,
    active: bool,
    out_path: str,
    formats: list[str] = ["png"],
    display: bool = False,
):
    dataframe = df.copy()

    if active:
        dataframe = dataframe[dataframe["is_active_group"].map(lambda x: parse_bool(x))]
    else:
        dataframe = dataframe[
            dataframe["is_active_group"].map(lambda x: not parse_bool(x))
        ]

    session_cols = [
        col for col in dataframe.columns if col.startswith("mean_bias_score (session ")
    ]

    long_df = dataframe.melt(
        value_vars=session_cols,
        var_name="session",
        value_name="score",
    )

    long_df["session"] = long_df["session"].str.extract(r"session (\d+)").astype(int)

    plt.figure(figsize=(8, 5))

    plot(long_df)
    plt.ylim(0, 1.1)

    if active:
        plt.title("Automation Bias Across Sessions (Active Group)")
    else:
        plt.title("Automation Bias Across Sessions (Control Group)")
    plt.xlabel("Session")
    plt.ylabel("Mean Automation Bias")

    plt.tight_layout()

    for fmt in formats:
        plt.savefig(f"{out_path}.{fmt}", dpi=300, bbox_inches="tight")

    if display:
        plt.show()

    plt.close()

def session_plot(
    df: pd.DataFrame,
    session: int,
    out_path: str,
    formats: list[str] = ["png"],
    display: bool = False,
):
    dataframe = df.copy()

    dataframe["group"] = dataframe["is_active_group"].map(
        lambda x: "Active" if parse_bool(x) else "Control"
    )

    score_col = f"mean_bias_score (session {session})"

    plt.figure(figsize=(6, 5))
    sns.boxplot(data=dataframe, x="group", y=score_col)
    plt.ylim(0, 1.1)

    plt.title(f"Session {session}: Automation Bias")
    plt.xlabel("")
    plt.ylabel("Mean Automation Bias")

    plt.tight_layout()

    for fmt in formats:
        plt.savefig(f"{out_path}.{fmt}", dpi=300, bbox_inches="tight")

    if display:
        plt.show()

    plt.close()
