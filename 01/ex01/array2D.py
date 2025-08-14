import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	"""    Takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and end arguments"""

	try:
		assert isinstance(family, list), "Input is not a list"
		assert isinstance(start, int) and isinstance(end, int), "Start or end is not a int"

		arr = np.array(family)
		print("My shape is :", arr.shape)
		s = slice(start, end)
		newArr = arr[s]
		print("My new shape is :", newArr.shape)
		return newArr.tolist()
	
	except Exception as e:
		print("AssertionError:", e)
		return None