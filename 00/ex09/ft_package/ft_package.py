def count_in_list(li: list, element_to_count):
	"""    Count element in a given list."""
	
	count = 0
	for element in li:
		if element == element_to_count:
			count += 1
	return count
