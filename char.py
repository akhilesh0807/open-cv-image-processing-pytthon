#import necsessary files
import numpy as np 
import cv2
#read the image using imread command
img=cv2.imread('CKOFy3m.jpg',1)

#convert color image to gray
img2gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#apply threshold
ret, mask= cv2.threshold(img,220,255,cv2.THRESH_BINARY)
#display image
cv2.imshow('charizard',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
