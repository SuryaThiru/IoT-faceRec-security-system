import numpy as np
import cv2

cap = cv2.VideoCapture("http://192.168.43.58:8080/video") # video capture source camera (Here webcam of laptop)
ret,frame = cap.read() # return a single frame in variable `frame`

while(True):
    cv2.imshow('img1',frame) #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
        cv2.imwrite('faces/shweta.jpg',frame)
        cv2.destroyAllWindows()
        break

cap.release()
