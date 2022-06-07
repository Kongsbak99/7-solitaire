from ImageRecognition.edgeDetectionLive2 import GetCardCorner
import cv2
from ImageRecognition.imageSplit import navn

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    navn(cap)
    cardCorner = GetCardCorner()
    cardCorner.GetCardCorner(frame)




    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# import numpy as np
# first_array = [1, 2, 3, 4, 5, 6]
# my_array = np.array(first_array)
#
# new_array = np.roll(my_array, 2)  # rotate right
# print(new_array)
#
# new_array = np.roll(my_array, -2)  # rotate left
# print(new_array)