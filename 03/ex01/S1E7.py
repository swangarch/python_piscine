from S1E9 import Character

class Baratheon(Character):
	"""Representing the Baratheon family."""

	def __init__(self, first_name, is_alive=True, family_name="Baratheon", eyes="brown", hairs="dark"):
		"""Inherent from character class, it takes _name, and optional is_alive, if is_alive not provided will be set to True."""

		if (not isinstance(first_name, str) or not isinstance(is_alive, bool)):
			raise Exception("Wrong parameter type for Baratheon.")
		if (not isinstance(family_name, str) or not isinstance(eyes, str) or not isinstance(hairs, str)):
			raise Exception("Wrong parameter type for Baratheon.")

		self.first_name = first_name
		self.is_alive = is_alive
		self.family_name = family_name
		self.eyes = eyes
		self.hairs = hairs

	def __str__(self):
		"""Return a string representaion of the instance."""

		return f'Lannister named {self.first_name} {self.family_name} is {"alive" if self.is_alive else "dead"} has {self.eyes} eyes, and {self.hairs} hairs.'

	def __repr__(self):
		"""Return a string representaion of the construction of instance."""

		return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})' 

class Lannister(Character):
	"""Representing the Lannister family."""
	
	def __init__(self, first_name, is_alive=True, family_name="Lannister", eyes="blue", hairs="light"):
		"""Inherent from character class, it takes _name, and optional is_alive, if is_alive not provided will be set to True."""

		if (not isinstance(first_name, str) or not isinstance(is_alive, bool)):
			raise Exception("Wrong parameter type for Lannister.")
		if (not isinstance(family_name, str) or not isinstance(eyes, str) or not isinstance(hairs, str)):
			raise Exception("Wrong parameter type for Lannister.")

		self.first_name = first_name
		self.is_alive = is_alive
		self.family_name = family_name
		self.eyes = eyes
		self.hairs = hairs

	def __str__(self):
		"""Return a string representaion of the instance."""

		return f'Lannister named {self.first_name} {self.family_name} is {"alive" if self.is_alive else "dead"} has {self.eyes} eyes, and {self.hairs} hairs.'

	def __repr__(self):
		"""Return a string representaion of the construction of instance."""

		return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

	@classmethod
	def create_lannister(cls, first_name, is_alive=True):
		"""Class method that allows to create Liannister in a chain."""

		return (cls(first_name, is_alive))

