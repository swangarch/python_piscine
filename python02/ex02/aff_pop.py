#!/usr/bin/python3

import matplotlib.pyplot as plt
from load_csv import load
import sys
import os


def convert_unit(x: str) -> float:
    """Take a number in string format digits or end with K as thousand or
    end with M as million, converts to direct number representation."""

    if (not isinstance(x, str)):
        raise Exception("Input not string.")
    elif (x[-1] == 'M'):
        return float(x[:-1]) * 1e6
    elif (x[-1] == 'k'):
        return float(x[:-1]) * 1e3
    else:
        return float(x)


def show_pop(file: str, region: list, colors: list) -> None:
    """Load a csv file with a path, retrive the region to display the
    population of the contry."""

    try:
        assert isinstance(file, str), "Wrong file path."
        assert os.path.exists(file), "Data file not exists."
        assert file.endswith(".csv"), "Not csv data."
        assert isinstance(region, list), "Wrong region type."
        assert isinstance(colors, list), "Wrong color type."
        assert len(region) == len(colors), "Mismatched data."
        assert all(isinstance(r, str) for r in region), "Not string in region."
        assert all(isinstance(c, str) for c in colors), "Not string in colors."

        df = load(file)
        if df is None:
            sys.exit(1)

        print(df)

        plt.figure(figsize=(12, 8))
        for i, country in enumerate(region):
            df_r = df.loc[country].apply(convert_unit)
            # apply convert_unit function to clean the raw data.
            df_r.index = df_r.index.astype(int)
            df_r = df_r[df_r.index <= 2050]
            # pandas boolean indexing, use bool list as index to filter
            plt.plot(df_r.index, df_r.values, label=country, color=colors[i])

        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.margins(x=0.05)

        xtick = [year for year in range(1800, 2050) if (year - 1800) % 40 == 0]
        plt.xticks(xtick)
        ytick = [a for a in range(int(2e7), int(7e7)) if (a - 2e7) % 2e7 == 0]
        ytick_formatted = [f"{int(t / 1e6)}M" for t in ytick]
        plt.yticks(ytick, ytick_formatted)

        plt.legend(loc="lower right")
        plt.show()

    except AssertionError as e:
        print("AssertionError:", e)

    except Exception as e:
        print("Error:", e)


def main():
    """Main function to show the France population."""

    regions = ["Belgium", "France"]
    colors = ["steelblue", "green"]
    show_pop("population_total.csv", regions, colors)


if __name__ == "__main__":
    main()
