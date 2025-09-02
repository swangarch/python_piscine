#!/usr/bin/python3

from load_csv import load


def main():
    """Main function to test if load function works correctly with csv file."""

    print(load("life_expectancy_years.csv"))

    print("-------------Error handle1--------------")
    print(load("filenotexist.csv"))
    print("-------------Error handle2--------------")
    print(load("tester.py"))


if __name__ == "__main__":
    main()
