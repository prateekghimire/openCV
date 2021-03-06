#Color detection

import cv2
import numpy as np

def empty(i):
    pass


cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar',640,240)
cv2.createTrackbar('Min Hue','TrackBar',0,179,empty)
cv2.createTrackbar('Max Hue','TrackBar',68,179,empty)
cv2.createTrackbar('Min Sat','TrackBar',144,255,empty)
cv2.createTrackbar('Max Sat','TrackBar',255,255,empty)
cv2.createTrackbar('Min Val','TrackBar',52,255,empty)
cv2.createTrackbar('Max Val','TrackBar',255,255,empty)

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

while True:
    img =cv2.imread('lambo.jpeg')
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    minhue=cv2.getTrackbarPos('Min Hue','TrackBar')
    maxhue=cv2.getTrackbarPos('Max Hue','TrackBar')
    minsat=cv2.getTrackbarPos('Min Sat','TrackBar')
    maxsat=cv2.getTrackbarPos('Max Sat','TrackBar')
    minval=cv2.getTrackbarPos('Min Val','TrackBar')
    maxval=cv2.getTrackbarPos('Max Val','TrackBar')
    
    lower=np.array([minhue,minsat,minval])
    upper=np.array([maxhue,maxsat,maxval])

    mask=cv2.inRange(imgHSV,lower,upper)
    resultimg=cv2.bitwise_and(img,img,mask=mask)

    #cv2.imshow('Image',img)
    #cv2.imshow('HSV Image',imgHSV)
    #cv2.imshow('Mask',mask)
    #cv2.imshow('Result',resultimg)

    result=stackImages(0.5,([img,imgHSV],[mask,resultimg]))
    cv2.imshow('Result',result)

    cv2.waitKey(1)

