from load_image import ft_show_img
from numpy import ndarray as array
import numpy as np

def ft_invert(array) -> array:
	"""Inverts the color of the image received."""

	newArr = 255 - array.copy()
	ft_show_img(newArr)
	return newArr

def ft_red(array) -> array:
	"""Converts the color of the image to red."""

	newArr = array.copy()
	newArr[:, :, 1] = 0
	newArr[:, :, 2] = 0

	ft_show_img(newArr)
	return newArr

def ft_green(array) -> array:
	"""Converts the color of the image to green."""

	newArr = array.copy()
	newArr[:, :, 0] = 0
	newArr[:, :, 2] = 0

	ft_show_img(newArr)
	return newArr

def ft_blue(array) -> array:
	"""Converts the color of the image to blue."""

	newArr = array.copy()
	newArr[:, :, 0] = 0
	newArr[:, :, 1] = 0

	ft_show_img(newArr)
	return newArr

def ft_grey(array) -> array:
	"""Converts the color of the image to grey."""

	newArr = (array.sum(axis=2) / 3).astype(np.uint8)

	ft_show_img(newArr)
	return newArr
