import cv2
import numpy as np 

img=cv2.imread('monalisa.jpg')

imgResize=cv2.resize(img,(300,200))

imgCropped=img[0:250,200:400]

#print(img.shape)
#print(imgResize.shape)

#cv2.imshow('Image',img)
cv2.imshow('Cropped Image',imgCropped)
cv2.waitKey(0)
