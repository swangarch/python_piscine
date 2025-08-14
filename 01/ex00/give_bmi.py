import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""    Accepts 2 lists of integers or floats in input and returns a list
	of BMI values."""
	
	try:
		assert isinstance(height, list), "Input not a list."
		assert all(isinstance(h, int) or isinstance(h, float) for h in height), "Wrong input type for height."
		assert all(isinstance(w, int) or isinstance(w, float) for w in weight), "Wrong input type for width."
		assert (len(weight) == len(height)), "List size not matched."

		arrH = np.array(height, dtype=float)
		arrW = np.array(weight, dtype=float)
		return (arrW / arrH ** 2).tolist()
	
	except Exception as e:
		print("AssertionError:", e)
		return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""    Accepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of booleans (True if above the limit)."""

	try:
		assert isinstance(bmi, list), "Input not a list."
		assert isinstance(limit, int), "Limit is not a int."
		assert all(isinstance(value, int) or isinstance(value, float) for value in bmi), "Wrong input type for height."

		return [value > limit for value in bmi]  

	except Exception as e:
		print("AssertionError:", e)
		return None