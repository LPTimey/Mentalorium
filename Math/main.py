from utils.collect_csv import collect_into
from utils.automationBiasGraph import print_formula_graph


def main():
    print_formula_graph("out/min automation bias graph.png")
    participants, dataframe = collect_into("out/collected.csv")


if __name__ == "__main__":
    main()
