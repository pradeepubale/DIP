import cv2 as cv
 
# 1. Reading images from file

img = cv.imread('images/cat02.jpg')

cv.imshow('Cat', img)

cv.waitKey(0) # wait for specific delay(time in msec) for a key to be pressed  0-> wait infinite amount of time
