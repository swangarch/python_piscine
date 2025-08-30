#!/usr/bin/python3

import numpy as np
from PIL import Image
from numpy import ndarray as array
import matplotlib.pyplot as plt
import sys


def ft_show_img(imgArr: array, title: str) -> None:
    """Function to show image, takes image array and title as input."""

    plt.title(title)
    if len(imgArr.shape) == 3:
        plt.imshow(imgArr.squeeze())
    elif len(imgArr.shape) == 2:
        plt.imshow(imgArr, cmap='grey')
    else:
        raise Exception("Wrong shape array.")
    plt.show()


def ft_load(path: str) -> array | None:
    """Function that loads an image with path, prints its format,
    and its pixels content in RGB format. The function works with
    JPG and JPEG format."""

    try:
        img = Image.open(path)
        arr = np.array(img)
        print("The shape of image is:", arr.shape)
        print(arr)
        ft_show_img(arr, "Figure VIII.1: Original")
        return arr

    except Exception as e:
        print("Error load:", e)
        sys.exit(1)
