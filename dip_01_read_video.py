import cv2 as cv

# 2. reading videos. 0- Webcam, 1- inbuilt cam of comp, 2- another cam

capture = cv.VideoCapture('images/rain.mp4') # or we can directly provide videos also

while True:
	isTrue, frame = capture.read()
	
	cv.imshow('Video', frame)
	
	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()
cv.destroyAllWindows()


### error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'imshow'
# It means file path to image or video is wrong or
# the video is ended & couldn't find more frames
