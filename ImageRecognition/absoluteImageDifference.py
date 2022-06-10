import os

import numpy as np
import cv2
from cv2 import absdiff

path = os.path.dirname(os.path.abspath(__file__))
pathname= path + '/ValidationImages/'
imageformat = ".jpg"
knight = cv2.imread('knight3.jpg')
trainimage1 = cv2.imread(pathname+"h4.jpg")

class PlaceholderCards:
    def __init__(self):
        self.image = []
        self.name = ""

def loadTrainingCards():
    path = os.path.dirname(os.path.abspath(__file__))
    pathname= path + '/ValidationImages/'
    imageformat = ".jpg"
    i=0
    validation_cards = []

    for Cards in ["c2","c3","c4","c5","c6","c7","c8","c9","c10","cj","cq","ck","ca"]:
        validation_cards.append(PlaceholderCards())
        validation_cards[i].name = Cards
        imageName = validation_cards[i].name + imageformat
        validation_cards[i].image = pathname + imageName
        imageFileLocation = validation_cards[i].image
        #print(validation_cards[i].image)
        i = i + 1

    return validation_cards





#    image1 = cv2.imread(validation_cards[1].image,cv2.imread(imageFileLocation))

def bestCardMatch(image):

    baseDiff = 10000

    #for Cards in loadTrainingCards():
        #diff_img = cv2.absdiff(image,Cards.image)
        #rank_diff = int(np.sum(diff_img) / 255)
       # if rank_diff < baseDiff:
         #   baseDiff = rank_diff
        #cv2.imread(Cards.image)
        #cv2.imshow("absc",Cards.image)
        #print(Cards.image)
        #cv2.imread(Cards.image)
       # cv2.imread(Cards.image)
        #print(rank_diff)

        #cv2.imshow("h",Cards.image)


   # return rank_diff









def showCardsDiff():
    knight = cv2.imread('knight3.jpg')
    knight2 = cv2.imread('knight4.jpg')
    heart10 = cv2.imread('10heart.jpg')
    diffTest1 = absdiff(knight, knight2)
    diffTest2 = absdiff(knight, heart10)
    valueCalc1 = int(np.sum(diffTest1) / 255)
    valueCalc2 = int(np.sum(diffTest2) / 255)
    print("Difference between knight & knight2 is:",valueCalc1)
    print("Difference between knight & heart10 is:",valueCalc2)

while 1:
    cv2.imshow("abc", trainimage1)
    if cv2.waitKey(1) & 0xFF == ord('r'):

        bestCardMatch(trainimage1)
        #loadTrainingCards()
       # cv2.imshow("abc",trainimage1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

