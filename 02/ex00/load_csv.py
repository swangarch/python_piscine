import pandas as pd

def load(path: str): # -> Dataset: #(You have to adapt the type of return according to your library
	"""Load a csv file and get it's pandas.dataframe object"""
	
	try:
		dataframe = pd.read_csv(path, header=0, index_col=0)
		return dataframe
	
	except Exception as e:
		print("Error:", e)
		return None