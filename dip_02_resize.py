# Program for resizing and rescaling

import cv2 as cv

def rescaleFrame(frame, scale=0.75):
	# works with Images, videos and Live videos
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)
	
	dimensions = (width, height) # make tuple
	
	return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

def changeRes(width, height):
	# works with only Live videos (Webcam or other live cam)
	capture.set(3, width)
	capture.set(4, height)


# reading videos
capture = cv.VideoCapture('images/rain.mp4') 

while True:
	isTrue, frame = capture.read()
	
	frame_resized = rescaleFrame(frame, scale=0.40)
	
	cv.imshow('Video', frame)
	cv.imshow('Video Resized', frame_resized)
	
	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()
cv.destroyAllWindows()
