from edgeDetectionLive2 import GetCardCorner
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while(1):
    _, frame = cap.read()
    cardCorner = GetCardCorner()
    cardCorner.GetCardCorner(frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
