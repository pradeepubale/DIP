# Imp functions in cv liabrary

import cv2 as cv

img = cv.imread('images/cat01.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Cat', gray)

# Blur an image (kernel val tuple should be an odd value)
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blurred cat", blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edge Detection of Cat', canny)

# Dilating the image (use canny images)
dilated = cv.dilate(canny, (5, 5), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding 
eroded = cv.erode(dilated, (5, 5), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500))
cv.imshow('Resized', resized)

# cropping
cropped = img[200:600, 300:800]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
