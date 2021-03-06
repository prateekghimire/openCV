#Contour and Shape detection

import cv2
import numpy as np 

img=cv2.imread('shapes.jpeg')
imgGS=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGS,(7,7),1)


def getContour(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area=cv2.contourArea(cnt)
        #print(area)
           
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(0,0,0),3) 
            perimeter=cv2.arcLength(cnt,True)
            #print(perimeter)
            approx=cv2.approxPolyDP(cnt,0.02*perimeter,True)
            #print(len(approx))  #Printing the number of edges/curve
            objcorners=len(approx)
            x, y, w, h =cv2.boundingRect(approx)
            if objcorners==3: ObjectType="Triangle"
            elif objcorners==8: ObjectType="Circle"
            elif objcorners==4:
                ratio=w/float(h)
                if ratio>0.95 and ratio<1.05:
                    ObjectType="Square"
                else:
                    ObjectType="Rectangle"
            #cv2.rectangle(imgContour,(x,y),(x+w,y+h),(150,150,30),2)
            cv2.putText(imgContour,ObjectType,(x+(w//2)-50,y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)


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

imgCanny=cv2.Canny(imgBlur,55,55)
imgBlank=np.zeros_like(img)
imgContour=img.copy()
getContour(imgCanny)


resultimage=stackImages(0.5,([img,imgGS,imgBlur],[imgCanny,imgContour,imgBlank]))

cv2.imshow('Output',resultimage)

cv2.waitKey(0)