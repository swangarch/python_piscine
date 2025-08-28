#!/usr/bin/python3

import numpy as np
from PIL import Image


def ft_load(path: str): #(you can return to the desired format)
	"""    a function that loads an image, prints its format, and its pixels
    content in RGB format.
    You have to handle, at least, JPG and JPEG format."""

	try:
		img = Image.open(path)
		arr = np.array(img)
		return arr

	except Exception as e:
		print("Error:", e)
		return None


def ft_show_img(imgArr) -> None:
	"""Function to show image."""

	newImgT = Image.fromarray(imgArr)
	newImgT.show()