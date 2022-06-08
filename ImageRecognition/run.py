import numpy as np
from cv2 import absdiff

from edgeDetectionLive2 import GetCardCorner
import cv2
import Images
from ImageRecognition.imageSplit import navn
knight = cv2.imread('knight3.jpg')
knight2 = cv2.imread('knight4.jpg')
heart10 = cv2.imread('10heart.jpg')
gray = cv2.cvtColor(knight, cv2.COLOR_BGR2GRAY)



cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
count = 0
while 1:

    _, frame = cap.read()
    listOfFrames = navn(frame)

    cv2.imshow('preview', frame)

    # cv2.imshow(1, listOfFrames[1])
    # for i in range(0, len(listOfFrames)):
    #     #cv2.imshow(str(i), listOfFrames[i])
    #     cardCorner = GetCardCorner(listOfFrames[i])
    #     cv2.imshow((str(i), frame))
    if cv2.waitKey(1) & 0xFF == ord('r'):
        box1 = GetCardCorner(listOfFrames[7])
        box2 = GetCardCorner(listOfFrames[8])
        box3 = GetCardCorner(listOfFrames[9])
        box4 = GetCardCorner(listOfFrames[10])
        #cv2.imshow("num1", box1)
        cv2.imshow("num2", box2)
        cv2.imshow("num3", box3)
        cv2.imshow("num4", box4)
        cv2.imshow("knight", knight)

       # diff_img = cv2.absdiff(knight, gray)
       # rank_diff = int(np.sum(diff_img))
        diffTest1 = absdiff(knight, knight2)
        diffTest2 = absdiff(knight, heart10)
        valueCalc1 = int(np.sum(diffTest1)/255)
        valueCalc2 = int(np.sum(diffTest2) / 255)
        print(valueCalc1)
        print(valueCalc2)


       # print(int(knight))

        try:
            #cardCornerPicture = GetCardCorner(frame)
            #bw_filter = bw_filter(box1)

            cv2.imwrite("TrainingImages/frame%d.jpg" % count, box2)  # save frame as JPEG file
            cv2.imshow('CardCornerPicture', box2)  # Display the resulting frame

            count += 1
                #continue
        except:
            print("Could not find card corner")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break