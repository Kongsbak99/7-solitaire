import os
import random

from matplotlib import pyplot as plt

from ImageRecognition.CardDetection import ObjectDetection
from ImageRecognition.featureMatching2 import Person, matchcard
from ImageRecognition.write_on_image import write_on_image
from edgeDetectionLive2 import GetCardCorner
import cv2
from ImageRecognition.imageSplit import navn

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


class Cards:
    def __init__(self, row, card):
        self.row = row
        self.card = card


listofResults = []


def run():
    listOfCorners = []

    for i in range(len(listOfFrames)):
        listOfCorners.append(GetCardCorner(listOfFrames[i]))

    # Create a new object and execute.
    for i in range(len(listOfCorners)):
        try:
            detector = ObjectDetection(capture_index=listOfCorners[i], model_name=True)
            card = detector()
            listofResults.append(Cards(i, card))
        except:
            print("Detector error")

    print("Printing list of cards")
    for obj in listofResults:
        print(str(obj.row) + " " + obj.card)

while 1:
    _, frame = cap.read()
    listOfFrames = navn(frame)
    for i in range(len(listofResults)):
       write_on_image(frame, listofResults[i].row, listofResults[i].card)
    cv2.imshow('preview', frame)

    if cv2.waitKey(1) & 0xFF == ord('r'):
        cv2.imshow('preview', frame)
        run()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break