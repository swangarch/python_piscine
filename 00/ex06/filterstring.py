import sys
import re
from ft_filter import ft_filter

if (__name__ == "__main__"):
	try:
		assert (len(sys.argv) == 3 and re.fullmatch(r'[A-Za-z0-9\s]+', sys.argv[1]) and re.fullmatch(r'-?\d+', sys.argv[2])), "the arguments are bad"
		
	except AssertionError as e:
		print("AssertionError:", e)
		sys.exit(1)
	
	try:
		tab = sys.argv[1].split()
		threshold = int(sys.argv[2])
		tabAfter = list(ft_filter(lambda s: len(s) > threshold, tab))
		print(tabAfter)
	except Exception as e:
		print("Error:", e)
		sys.exit(1)
