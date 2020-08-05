#Face Detection

import cv2
import numpy as np

faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread('people.jpg')
imgGS=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=faceCascade.detectMultiScale(imgGS,1.1,4) 

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow('Face',img)
#cv2.imshow('GrayScale',imgGS)
cv2.waitKey(0)