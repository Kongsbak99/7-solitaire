from ImageRecognition.edgeDetectionLive2 import GetCardCorner
import cv2
import keyboard

cap = cv2.VideoCapture(0)
count = 0

while (1):
    _, frame = cap.read()
    cardCorner = GetCardCorner()
    CardCornerPicture = cardCorner.GetCardCorner(frame)

    key = cv2.waitKey(33) & 0b11111111
    if key == ord('q'):

        cv2.imwrite("TrainingImages/frame%d.jpg" % count, CardCornerPicture)  # save frame as JPEG file
        count += 1
        # Display the resulting frame
        cv2.imshow('CardCornerPicture', CardCornerPicture)

        continue

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
