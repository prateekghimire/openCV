import cv2
import numpy as np

video=cv2.VideoCapture(0)
video.set(3,800)
video.set(4,800)
video.set(10,50)     #Set Brightness in video
faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



while True:
    success,img=video.read()
    imgGS=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(imgGS,1.3,5) 

    if(len(faces)==0):
        cv2.putText(img,"No Face Detected",(20,40),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
        cv2.putText(img,'Face Detected',(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.putText(img,'Total Face : '+str(len(faces)),(280,446),cv2.FONT_HERSHEY_PLAIN,1.5,(255,0,0),3)

    cv2.imshow('Face Detection',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()