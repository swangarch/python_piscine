#!/usr/bin/python3

import sys
from load_image import ft_load
import matplotlib.pyplot as plt
from numpy import ndarray as array


def ft_crop(imgArr: array, startX: int, startY: int, sizeX: int, sizeY: int) \
        -> array:
    """Function to crop a image array, return a new array"""

    return imgArr[startY:startY + sizeY, startX:startX + sizeX, 0:1]


def main():
    """Program to load animal.jpeg, image has to be put at the same directory
    as the scripts. It displays the shape of image, the pixel content. Then
    slice the image, and displays image content and display image."""

    try:
        imgArr = ft_load("animal.jpeg")
        if imgArr is None:
            sys.exit(1)
        print(imgArr)
        newImgArr = ft_crop(imgArr, 450, 120, 400, 400)
        print("New shape after slicing:", newImgArr.shape)
        print(newImgArr)

        plt.imshow(newImgArr.squeeze(), cmap='grey')
        plt.show()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
