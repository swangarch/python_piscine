#!/usr/bin/python3

from numpy import ndarray as array
import numpy as np
from load_image import ft_show_img
import sys


def ft_invert(array: array) -> array:
    """Inverts the color of the image received."""

    try:
        newArr = 255 - array.copy()
        ft_show_img(newArr, "Figure VIII.2: Invert")
        return newArr
    except Exception as e:
        print("Error invert:", e)
        sys.exit(1)


def ft_red(array: array) -> array:
    """Converts the color of the image to red."""

    try:
        newArr = array.copy()
        newArr[:, :, 1] = 0
        newArr[:, :, 2] = 0

        ft_show_img(newArr, "Figure VIII.3: Red")
        return newArr
    except Exception as e:
        print("Error red:", e)
        sys.exit(1)


def ft_green(array: array) -> array:
    """Converts the color of the image to green."""

    try:
        newArr = array.copy()
        newArr[:, :, 0] = 0
        newArr[:, :, 2] = 0

        ft_show_img(newArr, "Figure VIII.4: Green")
        return newArr

    except Exception as e:
        print("Error green:", e)
        sys.exit(1)


def ft_blue(array: array) -> array:
    """Converts the color of the image to blue."""

    try:
        newArr = array.copy()
        newArr[:, :, 0] = 0
        newArr[:, :, 1] = 0

        ft_show_img(newArr, "Figure VIII.5: Blue")
        return newArr

    except Exception as e:
        print("Error blue:", e)
        sys.exit(1)


def ft_grey(array: array) -> array:
    """Converts the color of the image to grey."""

    try:
        newArr = array.copy()
        newArr = (newArr.sum(axis=2) / 3).astype(np.uint8)

        ft_show_img(newArr, "Figure VIII.6: Grey")
        return newArr

    except Exception as e:
        print("Error grey:", e)
        sys.exit(1)
