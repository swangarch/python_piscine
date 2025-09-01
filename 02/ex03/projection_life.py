#!/usr/bin/python3

import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Load two table of income per person and life expectancy, visualize
the scatter of 1900, with x-axis GDP and y-axis life Expecancy."""

    df1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df2 = load("life_expectancy_years.csv")

    income = df1["1900"]
    life = df2["1900"]

    print("[INCOME 1900]", income.to_list()[:50], "...")
    print("[LIFE 1900]", life.to_list()[:50], "...")

    plt.scatter(income.values, life.values)
    plt.xlim(300, 10000)

    plt.xscale("log")
    # logarithmic relationship
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.show()


if __name__ == "__main__":
    main()
