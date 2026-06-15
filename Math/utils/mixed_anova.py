import pingouin as pg
import pandas as pd


def anova_into(
    df: pd.DataFrame, anova_path: str, descriptive_path: str, result_path: str
) -> (pd.DataFrame, pd.DataFrame, str):
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

    anova.to_csv(anova_path)

    print(anova)

    # ------------------------------------------

    # 6. Deskriptive Statistik

    # ------------------------------------------

    descriptives = long_df.groupby(["group", "session"])["bias"].agg(
        ["mean", "std", "count"]
    )

    print("\n===== DESKRIPTIVE STATISTIK =====")

    descriptives.to_csv(descriptive_path)
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

    with open(result_path, "w", encoding="utf-8") as f:
        print(res, file=f)

    print(res)
    return (anova, descriptives, res)
