#!/usr/bin/python3

import numpy as np


def check_rec(family: list) -> bool:
    """Test if an 2D array is rectangle."""

    return len({len(row) for row in family if isinstance(row, list)}) <= 1


def slice_me(family: list, start: int, end: int) -> list:
    """    Takes as parameters a 2D array, prints its shape,
    and returns a truncated version of the array based on the
    provided start and end arguments"""

    try:
        assert isinstance(family, list), "Input is not a list."
        assert isinstance(start, int), "Start is not a int."
        assert isinstance(end, int), "End is not a int."
        assert all(isinstance(row, list) for row in family), "Row not a list."
        assert check_rec(family), "Not rectangular."
        arr = np.array(family)
        assert len(arr.shape) == 2, "Not 2D array."

        print("My shape is :", arr.shape)
        s = slice(start, end)

        # slice object constructor slice(start, stop, step),
        # If indices in a slice are out of range, Python will automatically
        # truncate them to the valid boundaries without raise an error.

        newArr = arr[s]
        print("My new shape is :", newArr.shape)
        return newArr.tolist()

    except AssertionError as e:
        print("AssertionError:", e)
        return None

    except Exception as e:
        print("Error:", e)
        return None
