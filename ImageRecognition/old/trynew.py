import cv2
import numpy as np

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
h, w, c = frame.shape

blank = np.zeros((h, w, c), np.uint8)

n = 12
last = 0
for i in range(n + 1):
    w1 = w // n * (i + 1)

    sub_img = frame[:, last:w1]
    avg_color = cv2.mean(sub_img)
    blank[:, last:w1] = avg_color[:3]

    last = w1

cv2.imshow('opencv', blank)
cv2.waitKey(0)