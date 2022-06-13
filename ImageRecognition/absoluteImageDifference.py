import os

import numpy as np
import cv2

from ImageRecognition.old.image import bw_filter


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
    pathname = path + '/cardCutouts/'
    imageformat = ".jpg"
    i = 0
    validation_suits = []

    for Suits in ["spades", "clubs", "hearts", "diamonds"]:
        validation_suits.append(PlaceholderSuits())
        validation_suits[i].name = Suits
        imagename = validation_suits[i].name + imageformat
        validation_suits[i].image = cv2.imread(pathname + imagename)
        # print(imagename, Numbers, validation_numbers[i].image)
        i = i + 1

    return validation_suits



def loadTrainingNumbers():
    path = os.path.dirname(os.path.abspath(__file__))
    pathname = path + '/cardCutouts/'
    imageformat = ".jpg"
    i = 0
    validation_numbers = []

    for Numbers in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]:
        validation_numbers.append(PlaceholderNumbers())
        validation_numbers[i].name = Numbers
        imagename = validation_numbers[i].name + imageformat
        validation_numbers[i].image = cv2.imread(pathname + imagename)
        #print(imagename, Numbers, validation_numbers[i].image)
        i = i + 1

    return validation_numbers



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
        validation_cards[i].image = cv2.imread(pathname + imagename, cv2.COLOR_BGR2GRAY)
        i = i + 1

    return validation_cards


def bestCardMatch(image):

    baseDiff = 5000
    bestDiff = None
    bestCardName = None

    for Cards in loadTrainingCards():
        diff_img = cv2.absdiff(image, Cards.image)
        rank_diff = int(np.sum(diff_img) / 300)

        if rank_diff < baseDiff:
            bestDiff = rank_diff
            baseDiff = rank_diff

            #baseDiff = rank_diff
            bestCardName = Cards.name

            print(rank_diff,bestCardName)
    if bestDiff != None:

       print("Best matching card is", bestCardName, "& the value is:",bestDiff)

    #return bestCardName, bestDiff
