# Selecting random image from the database folder
# Emily Park

import cv2
import os
import random

def RandImage():
	dirName = 'Database'

	# Check if dirName is valid
	if not os.path.isdir(dirName):
		print("Unable to find directory")
		exit()

	# Select random number
	directory = os.listdir(dirName)
	dirSize   = len(directory)
	randNum   = random.randint(0, dirSize)

	# Select the image
	imgName = directory[randNum]
	imgName = os.path.join(dirName, imgName)

	# Load image and resize
	img = cv2.imread(imgName)
	height, width, channels = img.shape
	img = cv2.resize(img, (int((500/height) * width), 500))

	cv2.imshow('random image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	RandImage()