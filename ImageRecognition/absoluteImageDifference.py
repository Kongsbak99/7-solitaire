import os

import numpy as np
import cv2
from cv2 import absdiff


path = os.path.dirname(os.path.abspath(__file__))
pathname= path + '/ValidationImages/'
imageformat = ".jpg"
knight = cv2.imread(pathname+'d2.jpg',cv2.COLOR_BGR2GRAY)
knight.shape

class PlaceholderCards:
    def __init__(self):
        self.image = []
        self.name = ""

def loadTrainingCards():
    path = os.path.dirname(os.path.abspath(__file__))
    pathname= path + '/ValidationImages/'
    imageformat = ".jpg"
    i = 0
    validation_cards = []

    for Cards in ["c2","c3","c4","c5","c6","c7","c8","c9","c10","cj","cq","ck","ca"
                 ,"d2","d3","d4","d5","d6","d7","d8","d9","d10","dj","dq","dk","da"
                 ,"h2","h3","h4","h5","h6","h7","h8","h9","h10","hj","hq","hk","ha"
                 ,"s2","s3","s4","s5","s6","s7","s8","s9","s10","sj","sq","sk","sa"]:
        validation_cards.append(PlaceholderCards())
        validation_cards[i].name = Cards
        imagename = validation_cards[i].name + imageformat
        validation_cards[i].image = cv2.imread(pathname + imagename,cv2.COLOR_BGR2GRAY)
        i=i+1


    return validation_cards





#    image1 = cv2.imread(validation_cards[1].image,cv2.imread(imageFileLocation))

def bestCardMatch(image):

    baseDiff = 3000
    bestDiff = None
    bestCardName = "placeholder"
    for Cards in loadTrainingCards():
        diff_img = cv2.absdiff(image, Cards.image)
        rank_diff = int(np.sum(diff_img) / 300)

        if rank_diff < baseDiff:
            bestDiff = rank_diff
            bestCardName = Cards.name
    if bestDiff != None:
        print("Best matching card is", bestCardName, "& the value is:",bestDiff)











# def showCardsDiff():
#     knight = cv2.imread('knight3.jpg')
#     knight2 = cv2.imread('knight4.jpg')
#     heart10 = cv2.imread('10heart.jpg')
#     diffTest1 = absdiff(knight, knight2)
#     diffTest2 = absdiff(knight, heart10)
#     valueCalc1 = int(np.sum(diffTest1) / 255)
#     valueCalc2 = int(np.sum(diffTest2) / 255)
#     print("Difference between knight & knight2 is:", valueCalc1)
#     print("Difference between knight & heart10 is:", valueCalc2)



