import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
	#for puting on the web cam
	_,frame=cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	
	#for setting up of range
	lower_red=np.array([30,30,0])
	upper_red=np.array([180,255,255])
	
	#for setting up of range that we obtain above and using bitwise operator
	mask=cv2.inRange(hsv,lower_red,upper_red)
	res=cv2.bitwise_and(frame,frame,mask=mask)
	
	#for smoothning and removing background noise
	kernal=np.ones((15,15),np.float32)/225
	smoothed=cv2.filter2D(res,-1,kernal)
	
	cv2.imshow('frame',frame)
	cv2.imshow('ori',smoothed)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	k=cv2.waitKey(5) & 0xFF
	if k==27:
		break
	

cv2.destroyAllWindows()
cap.realease()