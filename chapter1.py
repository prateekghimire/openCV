import cv2

video=cv2.VideoCapture(0)
video.set(3,400)
video.set(3,640)
video.set(10,50)

while True:
    success, img =video.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    