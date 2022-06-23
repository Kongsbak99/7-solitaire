import os

import cv as cv
import numpy as np
import cv2

from ImageRecognition.old.image import bw_filter

"""""
Definitions are inspired by https://github.com/EdjeElectronics/OpenCV-Playing-Card-Detector
"""""

path = os.path.dirname(os.path.abspath(__file__))
pathname= path + '/cardCutouts/'

card = cv2.imread(pathname + "2.jpg")

#from ImageRecognition.old.edgeDetection import correctOrientation
#from ImageRecognition.old.image import bw_filter


class PlaceholderCards:
    def __init__(self):
        self.image = []
        self.name = ""


class PlaceholderNumbers:
    def __init__(self):
        self.image = []
        self.name = ""


class PlaceholderSuits:
    def __init__(self):
        self.image = []
        self.name = ""



def loadTrainingSuits():
    path = os.path.dirname(os.path.abspath(__file__))
    pathname = path + '/newCardCutouts/'
    imageformat = ".jpg"
    i = 0
    validation_suits = []

    for Suits in ["Spades", "Spades1","Spades_2","Spades_3", "Hearts","Hearts_1", "Diamonds","Diamonds_1","Diamonds_2","Diamonds_3","Diamonds_4","Diamonds_5", "Clubs", "Clubs1","Clubs_2","Clubs_3"]:
        validation_suits.append(PlaceholderSuits())
        validation_suits[i].name = Suits
        image_name = validation_suits[i].name + imageformat
        validation_suits[i].image = bw_filter(cv2.imread(pathname + image_name,cv2.COLOR_BGR2GRAY))
        #print(image_name, Suits, pathname + image_name)
        i = i + 1

    return validation_suits



def loadTrainingNumbers():
    path = os.path.dirname(os.path.abspath(__file__))
    pathname = path + '/newCardCutouts/'
    imageformat = ".jpg"
    i = 0
    validation_numbers = []

    for Numbers in ["2","2_1", "3","3_1","3_2","3_3", "4","4_1", "5","5_1","5_2","5_3", "6","6_1","6_2","6_3","6_4", "7", "8","8_1","8_2","8_3", "9","9_1","9_2", "10","10_1","10_2", "j", "q","q_1","q_2","q_3", "k","k_1", "a"]:
        validation_numbers.append(PlaceholderNumbers())
        validation_numbers[i].name = Numbers
        image_name = validation_numbers[i].name + imageformat
        validation_numbers[i].image = bw_filter(cv2.imread(pathname + image_name,cv2.COLOR_BGR2GRAY))
        #alidation_numbers[i].image = cv2.imread(pathname + image_name)
        #print(image_name, Numbers, pathname + image_name)
       # print(validation_numbers[i].image)
        i = i + 1

    return validation_numbers



# def loadTrainingCards():
#     path = os.path.dirname(os.path.abspath(__file__))
#     pathname= path + '/ValidationImages/'
#     imageformat = ".jpg"
#     i = 0
#     validation_cards = []
#
#
#     for Cards in ["c2","c3","c4","c5","c6","c7","c8","c9","c10","cj","cq","ck","ca"
#                  ,"d2","d3","d4","d5","d6","d7","d8","d9","d10","dj","dq","dk","da"
#                  ,"h2","h3","h4","h5","h6","h7","h8","h9","h10","hj","hq","hk","ha"
#                  ,"s2","s3","s4","s5","s6","s7","s8","s9","s10","sj","sq","sk","sa"]:
#         validation_cards.append(PlaceholderCards())
#         validation_cards[i].name = Cards
#         imagename = validation_cards[i].name + imageformat
#
#         validation_cards[i].image = bw_filter(cv2.imread(pathname + imagename,cv2.COLOR_BGR2GRAY))
#
#
#         i = i + 1
#     #test1=binary
#     #cv2.imshow("hey1",validation_cards[0].image)
#     #cv2.imshow("hey2", validation_cards[1].image)
#     #cv2.imshow("hey3", validation_cards[2].image)
#     #cv2.imshow("hey4", validation_cards[3].image)
#     #cv2.imshow("hey5", validation_cards[4].image)
#     #cv2.imshow("hey6", validation_cards[5].image)
#     #cv2.imshow("hey7", validation_cards[6].image)
#     return validation_cards


def bestCardMatch(image1,image2):

    baseNumDiff = 5000
    bestNumDiff = None
    bestCardNum = None

    baseSuitDiff = 5000
    bestSuitDiff = None
    bestCardSuit = None

    for Numbers in loadTrainingNumbers():
        diff_num = cv2.absdiff(image1, Numbers.image)
        numRankDiff = int(np.sum(diff_num) / 300)

        if numRankDiff > baseNumDiff:
            bestNumDiff = numRankDiff
            baseNumDiff = numRankDiff


            bestCardNum = Numbers.name

            #print(numRankDiff, bestCardNum)

    for Suits in loadTrainingSuits():
        diff_suit = cv2.absdiff(image2, Suits.image)
        rankSuitDiff = int(np.sum(diff_suit) / 300)

        if rankSuitDiff > baseSuitDiff:
            bestSuitDiff = rankSuitDiff
            baseSuitDiff = rankSuitDiff


            bestCardSuit = Suits.name

            #print(rankSuitDiff, bestCardSuit)
    print("hey",bestSuitDiff, bestNumDiff)
    if bestSuitDiff and bestNumDiff is not None:

       print("Best matching number is", bestCardNum, "& the value is:", bestNumDiff,
             "Best matching suit is", bestCardSuit, "& the value is:",bestSuitDiff)

    return bestCardNum, bestCardSuit, bestNumDiff, bestSuitDiff



corners = np.float32([[0,0],[0,420],[300,420],[300,0]])

cardCoordinates = np.float32([
    [0,0],
    [0,120],
    [100,120],
    [100,0]
])
# while 1:
#     loadTrainingSuits()
#
#     if cv2.waitKey(1) & 0xFF == ord('r'):
#         a=2
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#
#         break