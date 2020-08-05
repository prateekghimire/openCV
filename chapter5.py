import cv2
import numpy as np 

img=cv2.imread('cards.jpg')

width, height= 250,350
pts1=np.float32([[545,196],[695,229],[463,368],[627,414]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)

imgOut=cv2.warpPerspective(img,matrix,(width,height))

for i in range(0,len(pts1)):
    cv2.line(img,tuple(pts1[i]),tuple(pts1[i]),(255,0,0),thickness=8)

cv2.imshow('Window',img)
cv2.imshow('Warped Image',imgOut)
cv2.waitKey(0)