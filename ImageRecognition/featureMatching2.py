import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

from ImageRecognition.old.image import bw_filter


def matchcard(template, cardtomatch):
    MIN_MATCH_COUNT = 10
    #print(cardtomatch)
    newimg = bw_filter(cardtomatch)  # cv.imread(cardtomatch, 0)
    scale_percent = 60  # percent of original size
    width = int(newimg.shape[1] * scale_percent / 100)
    height = int(newimg.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    #resized = cv.resize(newimg, dim, interpolation=cv.INTER_AREA)

    # img1 = cv.imread('./Images/diamondenkel.jpg', 0)          # queryImage
    img1 = cv.imread(template, 0)  # queryImage
    img1 = bw_filter(img1)
    # img2 = cv.imread('./Images/diamond6rotated.jpg', 0)  # trainImage
    img2 = cardtomatch  # trainImage
    # Initiate SIFT detector
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(newimg, None)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    # store all the good matches as per Lowe's ratio test.
    good = []
    for m, n in matches:
        if m.distance < 0.4 * n.distance:
            good.append(m)

    if len(good) > MIN_MATCH_COUNT:
        """
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()
        h, w = img1.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv.perspectiveTransform(pts, M)
        img2 = cv.polylines(img2, [np.int32(dst)], True, 255, 3, cv.LINE_AA)
        #print("diamond six found")
        """
        #print("matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))
        matchesMask = None

    else:
        #print("Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))
        matchesMask = None

    draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                       singlePointColor=(255, 0, 0),
                       matchesMask=matchesMask,  # draw only inliers
                       flags=20)
    img3 = cv.drawMatches(img1, kp1, newimg, kp2, good, None, **draw_params)
    return Person(len(good), template, img3)


# matchcard()
class Person:
    def __init__(self, name, age, img):
        self.img = img
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

