from ImageRecognition.edgeDetectionLive2 import GetCardCorner
import cv2

cap = cv2.VideoCapture(1)

while(1):
    _, frame = cap.read()
    cardCorner = GetCardCorner()
    cardCorner.GetCardCorner(frame)


    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break