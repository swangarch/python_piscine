import matplotlib.pyplot as plt
from load_csv import load

def show_life_expec(file: str, region: str) -> None:
	"""Load a csv file with a path, retrive the region to display the life expectancy"""

	try:
		df = load(file)
		if not df is None:
			df_region = df.loc[region]
			df_region.plot(kind='line', title='France Life expectancy Projections', xlabel='Year', ylabel='Life expectancy', figsize=(12, 8))
			plt.show()

	except Exception as e:
		print("Error:", e)

def main():
	"""Main function to show the France life expectancy."""
	
	show_life_expec("life_expectancy_years.csv", "France")

if __name__ == "__main__":
	main()