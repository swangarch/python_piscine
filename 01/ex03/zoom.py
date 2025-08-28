#!/usr/bin/python3

from PIL import Image
from load_image import ft_load


def ft_crop(imgArr, startX, startY, sizeX, sizeY):
	"""Function to crop a image array, return a new array"""

	return imgArr[startY:startY + sizeY, startX:startX + sizeX, 0]


def main():  #create function
	try:
		imgArr = ft_load("animal.jpeg")
		print(imgArr)
		newImgArr = ft_crop(imgArr, 350, 160, 400, 400)
		print("New shape after slicing:", newImgArr.shape)
		print(newImgArr)

		newImg = Image.fromarray(newImgArr)
		newImg.show()
	
	except Exception as e:
		print("Error:", e)


if __name__ == "__main__":
	main()