import argparse
import pandas as pd
from glob import glob
from utils.participants import Participant


def collect_into(out_path: str) -> (list[Participant],pd.DataFrame):
    session1_files = glob("data/session 1/*.csv")
    session2_files = glob("data/session 2/*.csv")

    if not session1_files or not session2_files:
        raise FileNotFoundError("No CSV files found in one of the session folders.")

    df1 = pd.concat([pd.read_csv(f) for f in session1_files], ignore_index=True)
    df2 = pd.concat([pd.read_csv(f) for f in session2_files], ignore_index=True)

    df1["nickname"] = df1["nickname"].str.strip()
    df2["nickname"] = df2["nickname"].str.strip()

    merged = pd.merge(
        df1,
        df2,
        on="nickname",
        suffixes=("_s1", "_s2"),
        how="inner",
    )

    participants = []

    for _, row in merged.iterrows():
        row1 = row[[c for c in row.index if c.endswith("_s1")]].rename(lambda x: x[:-3])
        row2 = row[[c for c in row.index if c.endswith("_s2")]].rename(lambda x: x[:-3])

        for col in ["nickname", "age", "gender", "disclaimer (round 1)"]:
            if col in row:
                row1[col] = row[col]
                row2[col] = row[col]

        participants.append(Participant.from_df_rows(row1, row2))

    df_out = Participant.participants_to_df(participants)
    df_out.to_csv(out_path, index=False)

    return participants, df_out


def main():
    parser = argparse.ArgumentParser(
        description="Compare CSV data from two sessions by nickname."
    )
    parser.add_argument("out_path", help="output path for merged CSV")

    args = parser.parse_args()
    collect_into(args.out_path)


if __name__ == "__main__":
    main()
