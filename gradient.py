import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
	#img=cv2.imread('alia.jpg',1)
	_,frame=cap.read()
	
	laplacian=cv2.Laplacian(frame, cv2.CV_64F)
	sobelx= cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
	sobely= cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
	
	#edge detector built in function
	edges=cv2.Canny(frame,100,100)
	
	#cv2.imshow('imd',img)
	cv2.imshow('laplacian',laplacian)
	cv2.imshow('sobelx',sobelx)
	cv2.imshow('sobely',sobely)
	cv2.imshow('edges',edges)
	cv2.imshow('alia',edges)
	
	k=cv2.waitKey(5) & 0xFF
	if k==27:
		break

cv2.destroyAllWindows()