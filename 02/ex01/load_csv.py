#!/usr/bin/python3

import pandas as pd



def load(path: str) -> pd.DataFrame:
	"""Load a csv file and return it's pandas.DataFrame object."""
	
	try:
		df = pd.read_csv(path, header=0, index_col=0)
		print("Loading dataset of dimensions", df.shape)
		return df
	
	except Exception as e:
		print("Error:", e)
		return None
