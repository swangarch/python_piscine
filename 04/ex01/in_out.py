def square(x: int | float) -> int | float:
	"""Return the correspond square of input number, take int or float as parameters."""

	if not (isinstance(x, int) or isinstance(x, float)):
		print("Error: wrong input type.")
		return None
	return x ** 2

def pow(x: int | float) -> int | float:
	"""Return the correspond exponentiation of itself of an input number, take int or float as parameters."""

	if not (isinstance(x, int) or isinstance(x, float)):
		print("Error: wrong input type.")
		return None

	return x ** x

def outer(x: int | float, function) -> object:
		count = 0
	def inner() -> float: