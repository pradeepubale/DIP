# Drawing Shapes and Putting Text

import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') # np.zeros(ht, wdth, color_channels)
cv.imshow('Blank_Image', blank)

# Draw a Rectangle Syntax: cv.rectangle(img, start_pt, end_pt, color, thickness)

#cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
#cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=2)

# cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=-1) # thickness -1 OR cv.FILLED same result
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)

cv.imshow("Rectangle", blank)

# Draw a Circle Syntax: cv.circle(img, center, radious, color, thickness)
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=-1)
cv.imshow("Circle", blank)

# Draw a Line Syntax: cv.line(img, start_pt, end_pt, color, thickness)
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow("Line Draw", blank)

# Draw Text on an Image  Syntax: cv.putText(img, text, start_pt, fontFace, fontScale, color, thickness)
cv.putText(blank, 'Hello', (300, 300), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 255), 2)
cv.imshow("Text on blank img", blank)

cv.waitKey(0)
