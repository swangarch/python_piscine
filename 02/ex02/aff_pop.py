import matplotlib.pyplot as plt
import numpy as np
from load_csv import load

def convert_unit(x: str):
	"""Take a number in stroing format digits or end with K as thousand or end with M as million, converts to pure digits representation."""

	if (not isinstance(x, str)):
		raise Exception("Input not string.")
	elif (x[-1] == 'M'):
		return float(x[:-1]) * 1000000
	elif (x[-1] == 'k'):
		return float(x[:-1]) * 1000
	else:
		return float(x)

def show_pop(file: str, region: list, colors: list) -> None:
	"""Load a csv file with a path, retrive the region to display the population of the contry."""

	try:
		df = load(file)
		if not df is None:
			plt.figure(figsize=(12, 8))

			for i, country in enumerate(region):
				df_region = df.loc[country].apply(convert_unit)
				df_region.index = df_region.index.astype(float)
				df_region = df_region[df_region.index <= 2050]

				plt.plot(df_region.index, df_region.values, label=country, color=colors[i])

			plt.title('Population Projections')
			plt.xlabel('Year')
			plt.ylabel('Population')
			plt.margins(x=0.05)
			plt.xticks(np.arange(1800, 2051, 40))
			plt.legend(loc="lower right")

			plt.show()

	except Exception as e:
		print("Error:", e)

def main():
	"""Main function to show the France population."""
	
	show_pop("population_total.csv", ["France", "Belgium"], ["green", "cyan"])

if __name__ == "__main__":
	main()