from ft_package import count_in_list


def main():
	"""Main function to test the package."""

	try:
		print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
		print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
	except Exception as e:
		print("Error:", e)


if __name__ == "__main__":
	main()