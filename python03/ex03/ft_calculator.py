#!/usr/bin/python3

class calculator:
    """A calculator class support + - * / between objects."""

    def __init__(self, object):
        """Initialize calculator instance with an object as parameter."""

        self.object = object

    def __str__(self):
        return f'Calculator object which contains: {self.object}'

    def __repr__(self):
        return f'Vector: ({self.object})'

    def __add__(self, object) -> None:
        """Add with a passed scalar as parameter."""

        try:
            if not (isinstance(object, int) or isinstance(object, float)):
                raise TypeError("parameter not a number")
            self.object = [elem + object for elem in self.object]
            print(self.object)
        except Exception as e:
            print("Error", e)

    def __mul__(self, object) -> None:
        """Multiply with a passed scalar as parameter."""

        try:
            if not (isinstance(object, int) or isinstance(object, float)):
                raise TypeError("parameter not a number")
            self.object = [elem * object for elem in self.object]
            print(self.object)
        except Exception as e:
            print("Error", e)

    def __sub__(self, object) -> None:
        """Substract with a passed scalar as parameter."""

        try:
            if not (isinstance(object, int) or isinstance(object, float)):
                raise TypeError("parameter not a number")
            self.object = [elem - object for elem in self.object]
            print(self.object)
        except Exception as e:
            print("Error", e)

    def __truediv__(self, object) -> None:
        """Divided by a passed scalar as parameter, print error message when
        divide by zero."""

        try:
            if not (isinstance(object, int) or isinstance(object, float)):
                raise TypeError("parameter not a number")
            self.object = [elem / object for elem in self.object]
            print(self.object)
        except Exception as e:
            print("Error:", e)
