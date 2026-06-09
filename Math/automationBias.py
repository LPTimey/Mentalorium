import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import seaborn as sns
from scipy.stats import ttest_ind


MIN_BIAS = 0.25
A_BIAS = lambda i, r, c: (1 - i) * ((r - 1) / 4) * (c / 100)

OUTPATH = "out/AutomationBias/"
os.makedirs(OUTPATH, exist_ok=True)

PATHS = (
    "data/session 1/[SESSION 1] STUD Studie (German)_Submissions_2026-06-08.csv",
    "data/session 1/[SESSION 1] STUD Study (English)_Submissions_2026-06-08.csv",
    "data/session 1/[SESSION 1] STUD Study (Español)_Submissions_2026-06-08.csv",
    "data/session 2/[SESSION 2] STUD Study (German)_Submissions_2026-06-08.csv",
    "data/session 2/[SESSION 2] STUD Study (English)_Submissions_2026-06-08.csv",
    "data/session 2/[SESSION 2] STUD Study (Español)_Submissions_2026-06-08.csv",
)

CASE = (
    "case (round 1)",
    "case (round 2)",
    "case (round 3)",
)

ANSWER_CORRECT = (
    "correctness (round 1)",
    "correctness (round 2)",
    "correctness (round 3)",
)

DISCLAIMER_ON = (
    "disclaimer (round 1)",
    "disclaimer (round 2)",
    "disclaimer (round 3)",
)

RATING = (
    "rating (round 1)",
    "rating (round 2)",
    "rating (round 3)",
)

CONFIDENCE = (
    "confidence (round 1)",
    "confidence (round 2)",
    "confidence (round 3)",
)


def str_bool_to_float_series(s):
    return (
        s.astype(str)
        .str.strip()
        .str.lower()
        .map({
            "ja": 1,
            "yes": 1,
            "true": 1,
            "1": 1,
            "nein": 0,
            "no": 0,
            "false": 0,
            "0": 0
        })
        .fillna(0)
    )


def compute_biases(df):
    print("Columns loaded:", len(df.columns))

    for idx in range(3):
        rating_col = RATING[idx]
        conf_col = CONFIDENCE[idx]
        corr_col = ANSWER_CORRECT[idx]

        out_col = f"bias rating ({idx+1})"

        i = str_bool_to_float_series(df[corr_col])
        r = pd.to_numeric(df[rating_col], errors="coerce")
        c = pd.to_numeric(df[conf_col], errors="coerce")

        df[out_col] = (1 - i) * ((r - 1) / 4) * (c / 100)

    return df


def normalize_disclaimer(x):
    if pd.isna(x):
        return np.nan
    x = str(x).strip().lower()

    if x in ["ja", "yes", "true", "1"]:
        return 1
    if x in ["nein", "no", "false", "0"]:
        return 0
    return np.nan


def main():
    session1_list = []
    session2_list = []

    for path in PATHS:
        if not os.path.exists(path):
            print("Missing:", path)
            continue

        df = pd.read_csv(path, encoding="utf-8")

        if "session 1" in path.lower():
            session1_list.append(df)
        else:
            session2_list.append(df)

    # safe concat
    session1 = pd.concat(session1_list, ignore_index=True) if session1_list else pd.DataFrame()
    session2 = pd.concat(session2_list, ignore_index=True) if session2_list else pd.DataFrame()

    # compute bias
    session1 = compute_biases(session1)
    session2 = compute_biases(session2)

    # disclaimer normalization (round 1 only as currently defined)
    if not session1.empty:
        session1["DISCLAIMER"] = session1[DISCLAIMER_ON[0]].apply(normalize_disclaimer)
    if not session2.empty:
        session2["DISCLAIMER"] = session2[DISCLAIMER_ON[0]].apply(normalize_disclaimer)

    # bias columns
    bias_cols = [f"bias rating ({i+1})" for i in range(3)]

    # FIXED: mean only over non-zero bias values
    if not session1.empty:
        session1["bias_mean"] = session1.apply(
            lambda row: np.mean([row[c] for c in bias_cols if row[c] > 0]),
            axis=1
        )

    if not session2.empty:
        session2["bias_mean"] = session2.apply(
            lambda row: np.mean([row[c] for c in bias_cols if row[c] > 0]),
            axis=1
        )

    print("Done. Files saved.")

    session1["session"] = "Session 1"
    session2["session"] = "Session 2"

    #TODO: 3 boxplots
    # 1: session 1 disclaimer on vs disclaimer off
    # 2: disclaimer on Session 1 vs session 2
    # 2: disclaimer off Session 1 vs session 2

    combined = pd.concat(
        [
            session1[["nickname","session", "DISCLAIMER", "bias_mean"]],
            session2[["nickname","session", "DISCLAIMER", "bias_mean"]],
        ],
        ignore_index=True,
    )

    # ---------------------------------------
    # Nickname consistency check
    # ---------------------------------------

    names_s1 = set(session1["nickname"].dropna().astype(str).str.strip())
    names_s2 = set(session2["nickname"].dropna().astype(str).str.strip())

    only_s1 = sorted(names_s1 - names_s2)
    only_s2 = sorted(names_s2 - names_s1)

    print("\nParticipants in Session 1:", len(names_s1))
    print("Participants in Session 2:", len(names_s2))

    print("\nOnly in Session 1:")
    for n in only_s1:
        print("  ", n)

    print("\nOnly in Session 2:")
    for n in only_s2:
        print("  ", n)

    print(
        f"\nMatched participants: {len(names_s1.intersection(names_s2))}"
    )


    # remove rows without bias
    combined = combined.dropna(subset=["bias_mean"])

    # prettier labels
    combined["DISCLAIMER_LABEL"] = combined["DISCLAIMER"].map(
        {
            0: "Disclaimer Off",
            1: "Disclaimer On"
        }
    )

    #TODO: t & p tests pro Vergleich

    # ---------------------------------------
    # Plot 1
    # Session 1: Disclaimer On vs Off
    # ---------------------------------------

    plt.figure(figsize=(6, 5))

    sns.boxplot(
        data=combined[combined["session"] == "Session 1"],
        x="DISCLAIMER_LABEL",
        y="bias_mean",
    )

    plt.title("Session 1: Automation Bias")
    plt.xlabel("")
    plt.ylabel("Mean Automation Bias")

    plt.tight_layout()
    plt.savefig(
        os.path.join(OUTPATH, "boxplot_session1_disclaimer.png"),
        dpi=300,
    )
    plt.close()


    #TODO: fix because all session 1 actives also have false in Disclaimer Off in session 2
    # ---------------------------------------
    # Plot 2
    # Session 2: Disclaimer On vs Off
    # ---------------------------------------

    plt.figure(figsize=(6, 5))

    sns.boxplot(
        data=combined[combined["session"] == "Session 2"],
        x="DISCLAIMER_LABEL",
        y="bias_mean",
    )

    plt.title("Session 2: Automation Bias")
    plt.xlabel("")
    plt.ylabel("Mean Automation Bias")

    plt.tight_layout()
    plt.savefig(
        os.path.join(OUTPATH, "boxplot_session2_disclaimer.png"),
        dpi=300,
    )
    plt.close()

    #TODO: fix because all session 1 actives also have false in Disclaimer Off in session 2
    # ---------------------------------------
    # Plot 3
    # Disclaimer ON: Session 1 vs Session 2
    # ---------------------------------------

    plt.figure(figsize=(6, 5))

    sns.boxplot(
        data=combined[combined["DISCLAIMER"] == 1],
        x="session",
        y="bias_mean",
    )

    plt.title("Disclaimer ON")
    plt.xlabel("")
    plt.ylabel("Mean Automation Bias")

    plt.tight_layout()
    plt.savefig(
        os.path.join(OUTPATH, "boxplot_disclaimer_on.png"),
        dpi=300,
    )
    plt.close()

    # ---------------------------------------
    # Plot 4
    # Disclaimer OFF: Session 1 vs Session 2
    # ---------------------------------------

    plt.figure(figsize=(6, 5))

    sns.boxplot(
        data=combined[combined["DISCLAIMER"] == 0],
        x="session",
        y="bias_mean",
    )

    plt.title("Disclaimer OFF")
    plt.xlabel("")
    plt.ylabel("Mean Automation Bias")

    plt.tight_layout()
    plt.savefig(
        os.path.join(OUTPATH, "boxplot_disclaimer_off.png"),
        dpi=300,
    )
    plt.close()
    
    # export
    session1.to_csv("out/session1_output.csv", index=False)
    session2.to_csv("out/session2_output.csv", index=False)
    combined.to_csv("out/combined_output.csv", index=False)


if __name__ == "__main__":
    main()