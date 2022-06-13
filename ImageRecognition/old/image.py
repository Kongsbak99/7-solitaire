import cv2 as cv
import numpy as np


def bw_filter(frame):
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_GRAY2BGR)
    hsv = cv.cvtColor(hsv, cv.COLOR_BGR2HSV)
    # gray = cv.cvtColor(hsv, cv.COLOR_BGR2GRAY)
    # cv.imshow("grayscale", gray)
    # cv.imshow("HSV", hsv)

    # define range of red color in HSV
    # Threshold the HSV image to get only blue colors
    # Bitwise-AND mask and original image

    # lower red
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])

    # upper red
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    mask = cv.inRange(hsv, lower_red, upper_red)
    # res = cv.bitwise_and(frame, frame, mask=mask)

    mask2 = cv.inRange(hsv, lower_red2, upper_red2)
    # res2 = cv.bitwise_and(frame, frame, mask=mask2)

    # Black mask
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([179, 255, 155])

    mask3 = cv.inRange(hsv, lower_black, upper_black)
    # res3 = cv.bitwise_and(frame, frame, mask=mask3)

    img4 = cv.add(mask, mask2)
    img5 = cv.add(img4, mask3)

    # cv.imshow('Original',frame)
    # cv.imshow("black", mask3)
    #cv.imshow("combined", img5)
    # cv.imshow('red',img4)
    return img5

# Template matching har ikke scale variance - men kan til dels selv lave det
# Multitemplate matching (Needs pip install opencv-contrib-python )
# keypoints

# import cv2 as cv
# import numpy as np
#
# cap = cv.VideoCapture(0)
# while (1):
#     # Take each frame
#     _, frame = cap.read()
#     # Convert BGR to HSV
#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
#
#     # define range of red color in HSV
#     # Threshold the HSV image to get only blue colors
#     # Bitwise-AND mask and original image
#
#     # lower red
#     lower_red = np.array([0, 50, 50])
#     upper_red = np.array([10, 255, 255])
#
#     # upper red
#     lower_red2 = np.array([170, 50, 50])
#     upper_red2 = np.array([180, 255, 255])
#
#     mask = cv.inRange(hsv, lower_red, upper_red)
#     res = cv.bitwise_and(frame, frame, mask=mask)
#
#     mask2 = cv.inRange(hsv, lower_red2, upper_red2)
#     res2 = cv.bitwise_and(frame, frame, mask=mask2)
#
#     # Black mask
#     lower_black = np.array([0, 0, 0])
#     upper_black = np.array([179, 90, 90])
#
#     mask3 = cv.inRange(hsv, lower_black, upper_black)
#     res3 = cv.bitwise_and(frame, frame, mask=mask3)
#
#     img4 = cv.add(mask, mask2)
#     img5 = cv.add(img4, mask3)
#
#     cv.imshow('Original', frame)
#     cv.imshow("black", mask3)
#     cv.imshow("combined", img5)
#     cv.imshow('red', img4)
#
#     k = cv.waitKey(5) & 0xFF
#     if k == 27:
#         break
# cv.destroyAllWindows()