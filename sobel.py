import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('alia.jpg',1)

sobelx= cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely= cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imshow('img',img)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)

cv2.waitKey(0)
cv2.close