#!/usr/bin/python3

import matplotlib.pyplot as plt
from load_csv import load


def show_life_expec(file: str, region: str) -> None:
	"""Load a csv file with a path, retrive the region information to display the life expectancy"""

	try:
		df = load(file)
		print(df)
		# if df is not None:
		df_region = df.loc[region]
		df_region.plot(kind='line', title='France Life expectancy Projections', xlabel='Year', ylabel='Life expectancy', figsize=(12, 8))
		plt.show()

	except Exception as e:
		print("Error:", e)


def main():
	"""Program to show the France life expectancy."""
	
	show_life_expec("life_expectancy_years.csv", "France")


if __name__ == "__main__":
	main()