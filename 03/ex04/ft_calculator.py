#!/usr/bin/python3


class calculator:
    """Calculator class provides vector calculation static methods."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors, two identical length float list is required."""

        try:
            dp = sum([V1[i] * V2[i] for i in range(len(V1))])
            print("Dot product is:", dp)

        except Exception as e:
            print("Error:", e)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors, two identical length float list is required."""

        try:
            add = [float(V1[i] + V2[i]) for i in range(len(V1))]
            print("Add Vector is :", add)

        except Exception as e:
            print("Error:", e)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substract two vectors, two identical length float list is required."""

        try:
            sous = [float(V1[i] - V2[i]) for i in range(len(V1))]
            print("Sous Vector is:", sous)
        except Exception as e:
            print("Error:", e)