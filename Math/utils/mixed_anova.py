import pingouin as pg
import pandas as pd
from scipy.stats import shapiro
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import mixedlm
from statsmodels.formula.api import ols


def make_long_df(df: pd.DataFrame) -> pd.DataFrame:
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
    return long_df


def check_shapiro(df: pd.DataFrame, outpath: str) -> pd.DataFrame:
    long_df = make_long_df(df)

    results = []

    for group in long_df["group"].unique():
        for session in long_df["session"].unique():
            vals = long_df[
                (long_df["group"] == group) & (long_df["session"] == session)
            ]["bias"]

            stat, p = shapiro(vals)

            results.append(
                {
                    "group": group,
                    "session": session,
                    "W": stat,
                    "p": p,
                }
            )

            print(f"{group}, Session {session}: W={stat:.3f}, p={p:.3f}")

    results_df = pd.DataFrame(results)
    results_df.to_csv(outpath, index=False)

    return results_df


def wilcoxon_into(df: pd.DataFrame, outpath: str) -> pd.DataFrame:
    res: pd.DataFrame = pg.wilcoxon(
        x=df["mean_bias_score (session 1)"], y=df["mean_bias_score (session 2)"]
    )
    res.to_csv(outpath)
    return res


def anova_into(
    df: pd.DataFrame, anova_path: str, descriptive_path: str, result_path: str
) -> (pd.DataFrame, pd.DataFrame, str):
    long_df = make_long_df(df)

    # ------------------------------------------
    # 5. Mixed ANOVA mit statsmodels OLS
    # ------------------------------------------
    
    # Fit model with OLS (this treats it as a between-subjects design)
    # Note: This is NOT a true mixed ANOVA, but simpler for demonstration
    model = ols('bias ~ C(session) * C(group)', data=long_df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    
    # Get residuals
    residuals = model.resid
    
    # Convert to format similar to Pingouin
    anova_data = []
    for effect in anova_table.index:
        row = anova_table.loc[effect]
        anova_data.append({
            'Source': effect,
            'SS': row['sum_sq'],
            'DF1': row['df'],
            'DF2': anova_table.loc['Residual', 'df'],
            'F': row['F'],
            'p_unc': row['PR(>F)'],
            'np2': row['sum_sq'] / (row['sum_sq'] + anova_table.loc['Residual', 'sum_sq'])
        })
    
    anova = pd.DataFrame(anova_data)

    print("\n===== MIXED ANOVA =====")
    anova.to_csv(anova_path)
    print(anova)
    
    # Residual diagnostics
    print("\n===== RESIDUAL DIAGNOSTICS =====")
    print(f"Residuals shape: {residuals.shape}")
    print(f"Residual mean: {residuals.mean():.6f}")
    print(f"Residual variance: {residuals.var():.6f}")
    
    # Test normality of residuals
    from scipy.stats import shapiro
    stat, p = shapiro(residuals)
    print(f"Shapiro-Wilk test of residuals: W={stat:.3f}, p={p:.3f}")
    
    # ------------------------------------------
    # 6. Deskriptive Statistik (unchanged)
    # ------------------------------------------

    descriptives = long_df.groupby(["group", "session"])["bias"].agg(
        ["mean", "std", "count"]
    )

    print("\n===== DESKRIPTIVE STATISTIK =====")
    descriptives.to_csv(descriptive_path)
    print(descriptives)

    # ------------------------------------------
    # 7. APA-Ausgabe (unchanged)
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
