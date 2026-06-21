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

    # ensure bias score exists
    if "mean_bias_score" not in dataframe.columns:
        raise ValueError("mean_bias_score column missing in dataframe.")

    # --- create bins ---
    binned = pd.cut(dataframe["mean_usefulness"], bins=5)
    dataframe["usefulness_bin"] = binned

    # --- compute counts per bin ---
    counts = dataframe["usefulness_bin"].value_counts().sort_index()

    plt.figure(figsize=(7, 5))

    ax = sns.boxplot(
        data=dataframe, x="usefulness_bin", y="mean_bias_score", order=counts.index
    )

    # --- relabel x-axis with counts ---
    new_labels = [f"{interval}\n(n={counts[interval]})" for interval in counts.index]
    ax.set_xticklabels(new_labels)

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


def gender_score(
    df: pd.DataFrame,
    out_path: str,
    formats: list[str] = ["png"],
    display: bool = False,
):
    dataframe = df.copy()

    # --- normalize gender values ---
    gender_map = {
        "mann": "Male",
        "frau": "Female",
        "divers": "Non-Binary",
        "other": "Other",
        "will ich nicht sagen": "Private",
        "male": "Male",
        "female": "Female",
        "nonbinary": "Non-Binary",
        "other": "Other",
        "prefer not to say": "Private",
        "hombre": "Male",
        "mujer": "Female",
        "no binario": "Non-Binary",
        "otro": "Other",
        "prefiero no decirlo": "Private",
    }

    dataframe["gender"] = dataframe["gender"].str.lower().str.strip()
    dataframe["gender"] = dataframe["gender"].replace(gender_map)

    if "mean_bias_score" not in dataframe.columns:
        raise ValueError("mean_bias_score column missing in dataframe.")

    # --- compute counts per gender ---
    counts = dataframe["gender"].value_counts()

    # keep order consistent with plot
    order = counts.index.tolist()

    plt.figure(figsize=(7, 5))

    ax = sns.boxplot(data=dataframe, x="gender", y="mean_bias_score", order=order)

    # --- update x-axis labels with counts ---
    new_labels = [f"{g}\n(n={counts[g]})" for g in order]
    ax.set_xticklabels(new_labels)

    plt.title("Gender vs mean Automation Bias")
    plt.xlabel("Gender")
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

    # --- compute counts per session ---
    counts = long_df["session"].value_counts().sort_index()

    plt.figure(figsize=(8, 5))

    ax = plot(long_df)
    plt.ylim(0, 1.1)

    # --- relabel x-axis with counts ---
    new_labels = [f"{i}\n(n={counts[i]})" for i in sorted(counts.index)]
    ax.set_xticklabels(new_labels)

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

    # --- compute counts per group ---
    counts = dataframe["group"].value_counts()

    plt.figure(figsize=(6, 5))
    ax = sns.boxplot(data=dataframe, x="group", y=score_col)
    plt.ylim(0, 1.1)

    # --- relabel x-axis with counts ---
    new_labels = [f"{g}\n(n={counts[g]})" for g in ["Active", "Control"]]
    ax.set_xticklabels(new_labels)

    plt.title(f"Session {session}: Automation Bias")
    plt.xlabel("")
    plt.ylabel("Mean Automation Bias")

    plt.tight_layout()

    for fmt in formats:
        plt.savefig(f"{out_path}.{fmt}", dpi=300, bbox_inches="tight")

    if display:
        plt.show()

    plt.close()
