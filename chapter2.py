import cv2
import numpy as np

file="monalisa.jpg"
kernel=np.ones((5,5),np.uint8)

img=cv2.imread(file)
imgGS=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(img,(15,15),0)
imgCanny=cv2.Canny(img,150,150)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
imgErosion=cv2.erode(imgCanny,kernel,iterations=1)


#cv2.imshow('Original',img)
#cv2.imshow('Grayscale',imgGS)
#cv2.imshow('Blurred',imgBlur)
#cv2.imshow('Canny',imgCanny)
#cv2.imshow('Dilation on Canny',imgDialation)
cv2.imshow('Erosion on Canny',imgErosion)
cv2.waitKey(0)