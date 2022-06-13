import os

from matplotlib import pyplot as plt

from ImageRecognition.absoluteImageDifference import bestCardMatch
from ImageRecognition.featureMatching2 import Person, matchcard
from ImageRecognition.old.image import bw_filter
from ImageRecognition.write_on_image import write_on_image
from edgeDetectionLive2 import GetCardCorner
import cv2
from ImageRecognition.imageSplit import navn

path = os.path.dirname(os.path.abspath(__file__))
pathname= path + '/ValidationImages/'

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


def run():
    count = 0

    for i in range(0, 12):
        write_on_image(frame, i, count)

    box3 = GetCardCorner(listOfFrames[3])
    cv2.imshow("num3", box3)

    box0 = GetCardCorner(listOfFrames[0])
    box1 = GetCardCorner(listOfFrames[1])
    box2 = GetCardCorner(listOfFrames[2])
    box3 = GetCardCorner(listOfFrames[3])
    box4 = GetCardCorner(listOfFrames[4])
    box5 = GetCardCorner(listOfFrames[5])
    box6 = GetCardCorner(listOfFrames[6])
    box7 = GetCardCorner(listOfFrames[7])
    box8 = GetCardCorner(listOfFrames[8])
    box9 = GetCardCorner(listOfFrames[9])
    box10 = GetCardCorner(listOfFrames[10])
    box11 = GetCardCorner(listOfFrames[11])
    # cv2.imshow("num0", box0)
    # cv2.imshow("num1", box1)
    # cv2.imshow("num2", box2)
    cv2.imshow("num3", box3)
    # cv2.imshow("num4", box4)
    # cv2.imshow("num5", box5)
    # cv2.imshow("num6", box6)
    # cv2.imshow("num7", box7)
    # cv2.imshow("num8", box8)
    # cv2.imshow("num9", box9)
    # cv2.imshow("num10", box10)
    # cv2.imshow("num11", box11)
   # i=0
    #boxboxbox = [box0,box1,box2,box3,box4,box5,box6,box7,box8,box9,box10,box11]
    #for boxes in boxboxbox:

    if len(box3)==257:
        bestCardMatch(box3)

        #print("box:",i)
       # i=i+1


        #print(len(box3),"box3")

            #bestCardMatch(boxes)

    #p1 = Person(-1, "null", box0)

    # for filename in os.listdir("./ValidationImages"):
    #     if filename.endswith(".jpg"):
    #         p2 = matchcard("./ValidationImages/" + str(filename), box8)
    #         if p2.name > p1.name:
    #             p1 = p2
    #
    #         continue
    #     else:
    #         continue
    # plt.imshow(p1.img, 'gray'), plt.show(),
    # print(p1.name, p1.age)

    try:
        # cardCornerPicture = GetCardCorner(frame)
        # bw_filter = bw_filter(box1)

        # cv2.imwrite("TrainingImages/0frame%d.jpg" % count, box0)  # save frame as JPEG file
        # cv2.imwrite("TrainingImages/1frame%d.jpg" % count, box1)  # save frame as JPEG file
        # cv2.imwrite("TrainingImages/2frame%d.jpg" % count, box2)  # save frame as JPEG file
        # cv2.imwrite("TrainingImages/3frame%d.jpg" % count, box3)  # save frame as JPEG file
        # cv2.imwrite("TrainingImages/4frame%d.jpg" % count, box4)  # save frame as JPEG file
        # cv2.imwrite("TrainingImages/5frame%d.jpg" % count, box5)  # save frame as JPEG file
        # cv2.imwrite("TrainingImages/6frame%d.jpg" % count, box6)  # save frame as JPEG file
        # cv2.imwrite("TrainingImages/7frame%d.jpg" % count, box7)  # save frame as JPEG file
        # cv2.imwrite("TrainingImages/8frame%d.jpg" % count, box8)  # save frame as JPEG file
        # cv2.imwrite("TrainingImages/9frame%d.jpg" % count, box9)  # save frame as JPEG file
        # cv2.imwrite("TrainingImages/10frame%d.jpg" % count, box10)  # save frame as JPEG file
        # cv2.imwrite("TrainingImages/111frame%d.jpg" % count, box11)  # save frame as JPEG file
        # #cv2.imshow('CardCornerPicture', box3)  # Display the resulting frame

        count += 1
        # continue
    except:
        print("Could not find card corner")




while 1:
    _, frame = cap.read()
    listOfFrames = navn(frame)
    cv2.imshow('preview', frame)

    if cv2.waitKey(1) & 0xFF == ord('r'):
        cv2.imshow('preview', frame)
        run()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break
