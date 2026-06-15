from utils.collect_csv import collect_into
from utils.automationBiasGraph import print_formula_graph
import pingouin as pg
import pandas as pd


def main():
    print_formula_graph("out/min automation bias graph.png")
    participants, dataframe = collect_into("out/collected.csv")
    df = dataframe

    # ------------------------------------------

    # 2. Daten ins Long-Format bringen

    # ------------------------------------------

    long_df = pd.melt(
        df,
        id_vars=["nickname", "is_active_group"],
        value_vars=["mean_bias_score (session 1)", "mean_bias_score (session 2)"],
        var_name="session",
        value_name="bias",
    )

    # ------------------------------------------

    # 3. Session umkodieren

    # ------------------------------------------

    long_df["session"] = long_df["session"].str.extract(r"session (\d)").astype(int)

    # ------------------------------------------

    # 4. Gruppe umkodieren

    # ------------------------------------------

    long_df["group"] = long_df["is_active_group"].replace(
        {True: "Active", False: "Control", 1: "Active", 0: "Control"}
    )

    # ------------------------------------------

    # 5. Mixed ANOVA berechnen

    # ------------------------------------------

    anova: pd.DataFrame = pg.mixed_anova(
        data=long_df, dv="bias", within="session", between="group", subject="nickname"
    )

    print("\n===== MIXED ANOVA =====")

    anova.to_csv("out/Anova.csv")

    print(anova)

    # ------------------------------------------

    # 6. Deskriptive Statistik

    # ------------------------------------------

    descriptives = long_df.groupby(["group", "session"])["bias"].agg(
        ["mean", "std", "count"]
    )

    print("\n===== DESKRIPTIVE STATISTIK =====")

    descriptives.to_csv("out/Deskriptive.csv")
    print(descriptives)

    # ------------------------------------------

    # 7. APA-Ausgabe erzeugen

    # ------------------------------------------

    print("\n===== APA REPORT =====")

    res = ""

    for _, row in anova.iterrows():

        effect = row["Source"]

        F = row["F"]

        p = row["p_unc"]

        eta = row["np2"]

        df1 = int(row["DF1"])

        df2 = int(row["DF2"])

        res += (
            f"{effect}: "
            f"F({df1},{df2}) = {F:.2f}, "
            f"p = {p:.3f}, "
            f"η²p = {eta:.3f}\n"
        )

    with open("out/result.txt", "w", encoding="utf-8") as f:
        print(res, file=f)

    print(res)


if __name__ == "__main__":
    main()
