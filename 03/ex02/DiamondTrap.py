#!/usr/bin/python3

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True, family_name="Baratheon", eyes="brown", hairs="dark"):
        """Create an instance of a king."""
        
        super().__init__(first_name, is_alive, family_name, eyes, hairs)

    def __str__(self):
        """Return a string representaion of the instance."""

        return f'King named {self.first_name} {self.family_name} is {"alive" if self.is_alive else "dead"} has {self.eyes} eyes, and {self.hairs} hairs.'

    def __repr__(self):
        """Return a string representaion of the construction of instance."""

        return f'King({self.first_name}, {self.is_alive}, {self.family_name}, {self.eyes}, {self.hairs})' 

    def set_eyes(self, eyes: str) -> None:
        """Set the eye color of the king."""

        self.eyes = eyes
        return self

    def set_hairs(self, hairs: str) -> None:
        """Set the hair color of the king."""

        self.hairs = hairs
        return self
    
    def get_eyes(self) -> str:
        """Get the eye color of the king."""

        return self.eyes
    
    def get_hairs(self) -> str:
        """Get the hair color of the king."""

        return self.hairs