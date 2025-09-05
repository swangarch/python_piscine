#!/usr/bin/python3

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Create an instance of a king."""

        if not isinstance(first_name, str) or not isinstance(is_alive, bool):
            raise Exception("Wrong parameter type for King.")

        super().__init__(first_name, is_alive)

        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return a string representaion of the King instance."""

        out = f'King named {self.first_name} {self.family_name} '
        out += f'is {"alive" if self.is_alive else "dead"} has '
        out += f'{self.eyes} eyes, and {self.hairs} hairs.'
        return out

    def __repr__(self):
        """Return a string representaion of construction of King instance."""

        out = f'Vector: ({self.first_name}, {self.is_alive},'
        out += f'{self.family_name}, {self.eyes}, {self.hairs})'
        return out

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
