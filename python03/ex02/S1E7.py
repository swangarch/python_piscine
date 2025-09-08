#!/usr/bin/python3

from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Inherent from character class, it takes _name, and optional
        is_alive, if is_alive not provided will be set to True."""

        if not isinstance(first_name, str) or not isinstance(is_alive, bool):
            raise Exception("Wrong parameter type for Baratheon.")

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return a string representaion of the Baratheon instance."""

        out = f'Baratheon named {self.first_name} {self.family_name} '
        out += f'is {"alive" if self.is_alive else "dead"} has '
        out += f'{self.eyes} eyes, and {self.hairs} hairs.'

        return out

    def __repr__(self):
        """Return a string representaion of the construction of instance."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Inherent from character class, it takes _name, and optional
        is_alive, if is_alive not provided will be set to True."""

        if not isinstance(first_name, str) or not isinstance(is_alive, bool):
            raise Exception("Wrong parameter type for Lannister.")

        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return a string representaion of the Lannister instance."""

        out = f'Lannister named {self.first_name} {self.family_name} '
        out += f'is {"alive" if self.is_alive else "dead"} has '
        out += f'{self.eyes} eyes, and {self.hairs} hairs.'

        return out

    def __repr__(self):
        """Return a string representaion of the construction of instance."""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class method that allows to create Liannister in a chain."""

        return (cls(first_name, is_alive))
