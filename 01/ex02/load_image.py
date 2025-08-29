#!/usr/bin/python3

import numpy as np
from PIL import Image


def ft_load(path: str): #(you can return to the desired format)
	"""Function that loads an image, prints its format, and its pixels
    content in RGB format.
    You have to handle, at least, JPG and JPEG format."""

	try:
		img = Image.open(path)
		arr = np.array(img)
		print("The shape of image is:", arr.shape)
		return arr

	except Exception as e:
		print("Error:", e)
		return None
