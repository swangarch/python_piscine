def count_in_list(li: list, element_to_count: any) -> int | None:
	"""Count element in a given list return number, if input not valid, return None."""
	
	try:
		count = 0
		for element in li:
			if element == element_to_count:
				count += 1
		return count
	except Exception as e:
		print("Error:", e)
		return None
