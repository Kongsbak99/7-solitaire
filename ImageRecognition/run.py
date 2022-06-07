from ImageRecognition.edgeDetectionLive2 import GetCardCorner
import cv2
from ImageRecognition.imageSplit import navn

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while 1:
    _, frame = cap.read()
    listOfFrames = navn(frame)
    # navn(frame)
    # cardCorner = GetCardCorner()

    cv2.imshow('preview', frame)
    # cv2.imshow(1, listOfFrames[1])
    # for i in range(0, len(listOfFrames)):
    #     #cv2.imshow(str(i), listOfFrames[i])
    #     cardCorner = GetCardCorner(listOfFrames[i])
    #     cv2.imshow((str(i), frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        box1 = GetCardCorner(listOfFrames[7])
        box2 = GetCardCorner(listOfFrames[8])
        box3 = GetCardCorner(listOfFrames[9])
        box4 = GetCardCorner(listOfFrames[10])
        cv2.imshow("num1", box1)
        cv2.imshow("num2", box2)
        cv2.imshow("num3", box3)
        cv2.imshow("num4", box4)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
