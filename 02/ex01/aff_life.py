#!/usr/bin/python3

import matplotlib.pyplot as plt
from load_csv import load
import sys


def show_life_expec(file: str, region: str) -> None:
    """Load a csv file with a path, retrive the region information to
display the life expectancy"""

    try:
        df = load(file)
        if df is None:
            sys.exit(1)
        # print(df)
        df_r = df.loc[region]
        t = 'France Life expectancy Projections'
        x = 'Year'
        y = 'Life expectancy'
        df_r.plot(kind='line', title=t, xlabel=x, ylabel=y, figsize=(12, 8))
        plt.show()

    except Exception as e:
        print("Error:", e)


def main():
    """Program to show the France life expectancy."""

    show_life_expec("life_expectancy_years.csv", "France")


if __name__ == "__main__":
    main()
