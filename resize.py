import numpy as np
import cv2

img = cv2.imread('chem.jpg')
# we need to keep in mind aspect ratio so the image does
# not look skewed or distorted -- therefore, we calculate
# the ratio of the new image to the old image
r = (enter the width you want)/ img.shape[1]
dim = (enter width , int(img.shape[0]*r))
 
# perform the actual resizing of the image and show it
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


cv2.imshow("resized", resized)
cv2.imshow("img",img)
cv2.imwrite('chem1.png',resized)
cv2.waitKey(0)









