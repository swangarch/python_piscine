from PIL import Image
from load_image import ft_load

def main():  #create function
	try:
		imgArr = ft_load("animal.jpeg")
		print(imgArr)
		startX = 350
		startY = 160
		newImgArr = imgArr[startY:startY + 400, startX:startX + 400, 0]
		print("New shape after slicing:", newImgArr.shape)
		print(newImgArr)

		newImg = Image.fromarray(newImgArr)
		newImg.show()
	
	except Exception as e:
		print("Error:", e)

if __name__ == "__main__":
	main()