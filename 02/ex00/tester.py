#!/usr/bin/python3

from load_csv import load


def main():
    """Main function to test if load function works correctly with csv file."""

    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()