from utils.collect_csv import collect_into
from utils.graphs.automationBiasGraph import print_formula_graph
from utils.mixed_anova import anova_into, wilcoxon_into, check_shapiro
import utils.graphs.plots as plots
import pingouin as pg
import pandas as pd
import seaborn as sns
from pathlib import Path


def main():
    _, dataframe = collect_into("out/collected.csv")

    _ = check_shapiro(dataframe,"out/shapiro.csv")

    _ = wilcoxon_into(dataframe, "out/wilcoxon.csv")
    _, _, _ = anova_into(
        dataframe, "out/Anova.csv", "out/Deskriptive.csv", "out/result.txt"
    )

    # --------------------------------------------------------- #
    #                                                           #
    #                           Plots                           #
    #                                                           #
    # --------------------------------------------------------- #
    Path("out").mkdir(parents=True, exist_ok=True)
    print_formula_graph("out/min automation bias graph", ["png", "svg"])
    plots.mental_usefulness(
        dataframe,
        "out/corr_usefulness_bias",
        ["png", "svg"],
    )
    plots.gender_score(
        dataframe,
        "out/corr_gender_bias",
        ["png", "svg"],
    )

    Path("out/strip").mkdir(parents=True, exist_ok=True)
    plots.groups(
        lambda long_df: sns.stripplot(
            data=long_df, x="session", y="score", color="black", alpha=0.3
        ),
        dataframe,
        True,
        "out/strip/active",
        ["png", "svg"],
    )
    plots.groups(
        lambda long_df: sns.stripplot(
            data=long_df, x="session", y="score", color="black", alpha=0.3
        ),
        dataframe,
        False,
        "out/strip/control",
        ["png", "svg"],
    )

    Path("out/box").mkdir(parents=True, exist_ok=True)
    plots.groups(
        lambda long_df: sns.boxplot(
            data=long_df,
            x="session",
            y="score",
        ),
        dataframe,
        True,
        "out/box/active",
        ["png", "svg"],
    )
    plots.groups(
        lambda long_df: sns.boxplot(
            data=long_df,
            x="session",
            y="score",
        ),
        dataframe,
        False,
        "out/box/control",
        ["png", "svg"],
    )
    plots.session_plot(dataframe, 1, "out/box/session1", ["png", "svg"])
    plots.session_plot(dataframe, 2, "out/box/session2", ["png", "svg"])


if __name__ == "__main__":
    main()
