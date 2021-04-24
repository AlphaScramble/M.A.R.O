import cv2 
import numpy as np

def take_photos():

    kamera=cv2.VideoCapture(0)
    ret,kare=kamera.read()
    img=cv2.imwrite("resim.jpg",kare)
    kamera.release()
    cv2.destroyAllWindows()


