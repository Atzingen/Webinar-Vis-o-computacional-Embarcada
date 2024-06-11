#import opencv and numpy
import cv2  
import numpy as np

cv2.namedWindow('imagem', cv2.WINDOW_NORMAL)
cv2.resizeWindow('imagem', (1280, 720))
vid = cv2.VideoCapture(0)

def callback(x):
	global H_low,H_high,S_low,S_high,V_low,V_high
	H_low = cv2.getTrackbarPos('low H','controls')
	H_high = cv2.getTrackbarPos('high H','controls')
	S_low = cv2.getTrackbarPos('low S','controls')
	S_high = cv2.getTrackbarPos('high S','controls')
	V_low = cv2.getTrackbarPos('low V','controls')
	V_high = cv2.getTrackbarPos('high V','controls')


cv2.namedWindow('controls',2)
cv2.resizeWindow("controls", 550,10);

H_low = 0
H_high = 179
S_low= 0
S_high = 255
V_low= 0
V_high = 255

cv2.createTrackbar('low H','controls',0,179,callback)
cv2.createTrackbar('high H','controls',179,179,callback)

cv2.createTrackbar('low S','controls',0,255,callback)
cv2.createTrackbar('high S','controls',255,255,callback)

cv2.createTrackbar('low V','controls',0,255,callback)
cv2.createTrackbar('high V','controls',255,255,callback)


while(1):
	ret, frame = vid.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	hsv_low = np.array([H_low, S_low, V_low], np.uint8)
	hsv_high = np.array([H_high, S_high, V_high], np.uint8)

	mask = cv2.inRange(hsv, hsv_low, hsv_high)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('mask',mask)
	cv2.imshow('imagem',res)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

vid.release()	
cv2.destroyAllWindows()