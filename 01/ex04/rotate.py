#!/usr/bin/python3

import numpy as np
import sys
from load_image import ft_load
import matplotlib.pyplot as plt
from numpy import ndarray as array


def ft_crop(imgArr, startX, startY, sizeX, sizeY) -> array:
    """Function to crop a image array, return a new array."""

    return imgArr[startY:startY + sizeY, startX:startX + sizeX, 0:1]


def ft_transpose(imgArr) -> array:
    """Fucntion to transpose an 2 dimensional array."""

    assert len(imgArr.shape) == 2, "Not a 2 dimensional array."
    newArray = np.zeros(imgArr.shape[::-1], np.int32)

    for i, line in enumerate(newArray):
        for j in range(len(line)):
            newArray[i][j] = imgArr[j][i]
    return newArray


def main():
    """Main function to load animal.jpeg and rotate it, display original
    information and image."""

    try:
        imgArr = ft_load("animal.jpeg")
        if imgArr is None:
            sys.exit(1)
        newImgArr = ft_crop(imgArr, 450, 120, 400, 400)
        print("The shape of image is:", newImgArr.shape)
        print(newImgArr)

        newImgArrT = ft_transpose(newImgArr.squeeze())
        print("New shape after Transpose:", newImgArrT.shape)
        print(newImgArrT)

        plt.imshow(newImgArrT, cmap='grey')
        plt.show()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
