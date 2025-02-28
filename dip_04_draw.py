# Drawing Shapes and Putting Text

import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') # np.zeros(ht, wdth, color_channels)
cv.imshow('Blank_Image', blank)

# img = cv.imread('images/cat01.jpg')
# cv.imshow('Cat', img)

# 1. Paint the image to a crtain color
blank[:] = 0, 255, 0
cv.imshow('Green Image', blank)

blank[:] = 0, 0, 255
#blank[200:300, 300:500] = 0, 0, 255
cv.imshow('Red Image', blank)

blank[:] = 255, 0, 0
cv.imshow('Blue Image', blank)

cv.waitKey(0)
