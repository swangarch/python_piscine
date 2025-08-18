

class calculator:
	"""A calculator class support + - * /"""

	def __init__(self, object):
		""""""

		self.vec = object
	
	# def __str__(self):
		# """"""

	# def __repr__(self):
		# """"""

	def __add__(self, object) -> None: #type check
		""""""

		object = [elem + object for elem in self.vec]
		print(object)

	def __mul__(self, object) -> None:
		""""""

		object = [elem * object for elem in self.vec]
		print(object)
	
	def __sub__(self, object) -> None:
		""""""

		object = [elem - object for elem in self.vec]
		print(object)

	def __truediv__(self, object) -> None:
		""""""

		object = [elem / object for elem in self.vec]
		print(object)