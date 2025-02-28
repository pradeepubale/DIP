# Program for resizing and rescaling

import cv2 as cv

img = cv.imread('images/cat01.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	
	dimensions = (width, height) # make tuple
	
	return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Resized_Cat', resized_image)

cv.waitKey(0)
