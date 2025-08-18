from abc import ABC, abstractmethod

class Character(ABC):
	"""An abstract class, which has abstract method for constructor, and die method."""

	@abstractmethod
	def __init__(self, first_name, is_alive=True):
		"""Construct the abstract class Character, it takes _name, and optional is_alive, if is_alive not provided will be set to True, 
		the implementation has to be overwritten by child class."""
		
		pass
		
	
	def die(self):
		"""Change is_alive from True to False."""

		self.is_alive = False

class Stark(Character):
	"""A class inherent from abstract character class, has its own __init__ method and die method inherent from parent."""

	def __init__(self, first_name, is_alive=True):
		"""Inherent from character class, it takes _name, and optional is_alive, if is_alive not provided will be set to True."""

		if (not isinstance(first_name, str) or not isinstance(is_alive, bool)):
			raise Exception("Wrong parameter type for Stark.")
		self.first_name = first_name
		self.is_alive = is_alive