import numpy as np 
import cv2

img=cv2.imread('CKOFy3m.jpg',1)


img2gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, mask= cv2.threshold(img,220,255,cv2.THRESH_BINARY)

cv2.imshow('charizard',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
