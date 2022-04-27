from ImageRecognition.edgeDetectionLive2 import GetCardCorner

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
    cardCorner = GetCardCorner()

    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    (h, w) = frame.shape[:2]
    (cX, cY) = (w // 7, h // 4)
    #(dX, dY) = (w // 7, h // 5)
    # (aX, aY) = (w//7, h // 3)

  #  print(frame.shape)
  #  print(frame.size)

    Field1 = frame[cY:h, 0:cX]
    Field2 = frame[cY:h, cX:cX*2]
    Field3 = frame[cY:h, cX*2:cX*3]
    Field4 = frame[cY:h, cX*3:cX*4]
    Field5 = frame[cY:h, cX*4:cX*5]
    Field6 = frame[cY:h, cX*5:cX*6]
    Field7 = frame[cY:h, cX*6:cX*7]
    DrawField = frame[0:cY, 0:cX*2]
    AceStacks = frame[0:cY, cX*2:cX*6]


    if key == 27: # exit on ESC
        break
    else:

        cv2.rectangle(frame, (0, cY), (cX,h), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (cX, cY), (cX*2, h), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (cX*2, cY), (cX*3, h), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (cX*3, cY), (cX*4, h), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (cX*4, cY), (cX*5, h), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (cX*5, cY), (cX*6, h), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (cX*6, cY), (cX*7, h), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (0, 0), (cX*2, cY), color=(255, 0, 0), thickness=5)
        cv2.rectangle(frame, (cX*2, 0), (cX*6, cY), color=(255, 0, 0), thickness=5)

        #cv2.imshow("Field1", Field1)
        #cv2.imshow("Field2", Field2)
        #cv2.imshow("Field3", Field3)
        #cv2.imshow("Field4", Field4)
        #cv2.imshow("Field5", Field5)
        #cv2.imshow("Field6", Field6)
        #cv2.imshow("Field7", Field7)
        #cv2.imshow("Draw", DrawField)
        #cv2.imshow("AceStacks", AceStacks)

        cardCorner.GetCardCorner(AceStacks)

        #      cv2.imshow("Test77", Test8)



        from PIL import Image


        def crop(path, input, height, width, k, page, area):
            im = Image.open(input)
            imgwidth, imgheight = im.size
            for i in range(0, imgheight, height):
                for j in range(0, imgwidth, width):
                    box = (j, i, j + width, i + height)
                    a = im.crop(box)
                    try:
                        o = a.crop(area)
                        o.save(os.path.join(path, "PNG", "%s" % page, "IMG-%s.png" % k))
                    except:
                        pass
                    k += 1

vc.release()
cv2.destroyWindow("preview")