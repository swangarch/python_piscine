def ft_filter(function, iterable):
	"""filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
	
	if function is None:
		return (item for item in iterable if item)
	else:
		return (item for item in iterable if function(item))


# def isOdd(num: int) -> bool:
# 	if not isinstance(num, int):
# 		return False
# 	return (num % 2 == 1)
	
# def lessThanFiveChar(s : str) -> bool:
# 	if not isinstance(s, str):
# 		return False
# 	return len(s) < 5


# if __name__ == "__main__":
# 	print(filter.__doc__)

# 	print("............................................................")

# 	print(ft_filter.__doc__)

# 	print("____________________________________________________________")

# 	list1 = [True, False, True, False, False]
# 	print(list(filter(None, list1)))
# 	print(list(ft_filter(None, list1)))

# 	print("____________________________________________________________")

# 	list2 = [1, 4, 5, 6, 9]
# 	print(list(filter(isOdd, list2)))
# 	print(list(ft_filter(isOdd, list2)))

# 	print("____________________________________________________________")

# 	tuple1 = (1, "Hello world", "hello", "hi", "mov", "ecole42", "42", 42)
# 	print(tuple(filter(lessThanFiveChar, tuple1)))
# 	print(tuple(ft_filter(lessThanFiveChar, tuple1)))

# 	print("____________________________________________________________")