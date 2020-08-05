import cv2
import numpy as np
import time

img=np.zeros((512,512,3),np.uint8)
#img[:]=0,255,0
#print(img.shape)

cv2.line(img,(0,0),(512,512),(0,0,255),thickness=3)
cv2.rectangle(img,(200,200),(300,300),(255,0,0),cv2.FILLED)
cv2.circle(img,(256,256),200,(0,255,0),thickness=2)
cv2.putText(img,"openCV",(300,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),thickness=2)
cv2.imshow('ImageLine',img)
cv2.waitKey(0)

