import numpy as np
from PIL import Image
from load_image import ft_load ##do the medium

def ft_crop(imgArr, startX, startY, sizeX, sizeY):
	"""Function to crop a image array, return a new array"""

	assert startX <= imgArr.shape[1] and startY <= imgArr.shape[0], "Wrong crop size"
	assert startX <= imgArr.shape[1] - sizeX and startY <= imgArr.shape[0] - sizeY, "Wrong crop size"

	return imgArr[startY:startY + sizeY, startX:startX + sizeX]

def ft_transpose(imgArr):
	"""Fucntion to transpose an 2 dimensional array"""

	assert len(imgArr.shape) == 2, "Not a 2 dimensional array."
	newArray = np.ndarray(imgArr.shape[::-1], np.int32)

	for i, line in enumerate(newArray):
		for j in range(len(line)):
			newArray[i][j] = imgArr[j][i]
	return newArray


def main():
	try:
		imgArr = ft_load("animal.jpeg")
		newImgArr = ft_crop(imgArr, 350, 160, 400, 400)
		print("The shape of image is:", newImgArr.shape)
		print(newImgArr)

		newImgArrT = ft_transpose(newImgArr)
		print("New shape after Transpose:", newImgArrT.shape)
		print(newImgArrT)
		newImgT = Image.fromarray(newImgArrT)
		newImgT.show()
	
	except Exception as e:
		print("Error:", e)

if __name__ == "__main__":
	main()