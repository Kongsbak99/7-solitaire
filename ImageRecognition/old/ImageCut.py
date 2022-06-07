import os

import cv2
import argparse

cv2.namedWindow("preview")
vc = cv2.VideoCapture(1)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    (h, w) = frame.shape[:2]
    (cX, cY) = (w // 7, h // 5)
    (dX, dY) = (w // 7, h // 5)
    (aX, aY) = (w//7, h // 3)

  #  print(frame.shape)
  #  print(frame.size)

    Field1 = frame[cY:h, 0:cX]
    Field2 = frame[cY:h, cX:cX*2]
    Field3 = frame[cY:h, cX*2:cX*3]
    Field4 = frame[cY:h, cX*3:cX*4]
    Field5 = frame[cY:h, cX*4:cX*5]
    Field6 = frame[cY:h, cX*5:cX*6]
    Field7 = frame[cY:h, cX*6:cX*7]

    if key == 27: # exit on ESC
        break
    else:

        cv2.rectangle(frame, (0, 144), (182,720), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (182, 144), (364, 720), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (364, 144), (546, 720), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (546, 144), (728, 720), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (728, 144), (910, 720), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (910, 144), (1092, 720), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (1092, 144), (1274, 720), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (0, 0), (182, 144), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (182, 0), (910, 144), color=(255, 0, 0), thickness=5)

        cv2.imshow("Field1", Field1)
        cv2.imshow("Field2", Field2)
        cv2.imshow("Field3", Field3)
        cv2.imshow("Field4", Field4)
        cv2.imshow("Field5", Field5)
        cv2.imshow("Field6", Field6)
        cv2.imshow("Field7", Field7)