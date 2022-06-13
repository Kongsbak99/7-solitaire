import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#img1 = cv.imread('box.png', cv.IMREAD_GRAYSCALE)  # queryImage


# img2 = cv.imread('box_in_scene.png',cv.IMREAD_GRAYSCALE) # trainImage
from ImageRecognition.old.image import bw_filter


def BFMatcher(template_, cardtomatch_, tresh):
    #template = template_  #cv.imread('ValidationImages/d7.jpg', cv.IMREAD_GRAYSCALE)  # queryImage
    template = cv.imread(template_, 0)  # queryImage
    template = bw_filter(template)

    cardtomatch = cardtomatch_
    # Initiate SIFT detector
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(template, None)
    kp2, des2 = sift.detectAndCompute(cardtomatch, None)

    # BFMatcher with default params
    bf = cv.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < tresh * n.distance:
            good.append([m])
    # cv.drawMatchesKnn expects list of lists as matches.
    img3 = cv.drawMatchesKnn(template, kp1, cardtomatch, kp2, good, None, flags=cv.DrawMatchesFlags_DRAW_RICH_KEYPOINTS) #DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    #plt.imshow(img3), plt.show()
    print(template_ + " = " + str(len(good)))
    return bfmatch(len(good), img3, template_)


class bfmatch:
    def __init__(self, num, frame, name):
        self.frame = frame
        self.num = num
        self.name = name
