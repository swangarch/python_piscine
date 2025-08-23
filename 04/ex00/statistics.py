from typing import Any

###CHECK
def percentile(sorted_li: list, percentage: float) -> float:  
	"""Given a list a percentage, calculate its percentage"""

	length = len(sorted_li)
	i = int(percentage * length / 100.0)
	return i

def ft_statistics(*args: Any, **kwargs: Any) -> None:
	"""Statistics for the given numbers passed in front, followed by the operations passed as key value pair, it can take multiple numbers and operations at one time."""

	# add error check
	for k in kwargs:
		try:
			if kwargs[k] == "mean":
				if len(args) == 0:
					print("ERROR")
				else:
					print("mean :", sum(args) / len(args))

			elif kwargs[k] == "median":
				if len(args) == 0:
					print("ERROR")
				else:
					li = sorted(list(args))
					print("median :", li[int(len(li) / 2)])

			elif kwargs[k] == "quartile":
				if len(args) == 0:
					print("ERROR")
				else:
					li = sorted(list(args))
					
					print(f"quartile : [{float(li[percentile(li, 25)])}, {float(li[percentile(li, 75)])}]")

			elif kwargs[k] == "std":
				if len(args) == 0:
					print("ERROR")
				else:
					mean = sum(args) / len(args)
					var = sum((mean - num) ** 2 for num in args) / len(args)
					std = var ** 0.5	
					print("std :", std)
				
			elif kwargs[k] == "var":
				if len(args) == 0:
					print("ERROR")
				else:
					mean = sum(args) / len(args)
					var = sum((mean - num) ** 2 for num in args) / len(args)
					print("var :", var)
				
			else:
				pass

		except Exception as e:
			print("ERROR", e)
	
	
