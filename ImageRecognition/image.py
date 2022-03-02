import cv2 as cv
import time

cap = cv.VideoCapture(0)


#Reading the image from capture
img = cv.imread(cap)

 
cv.imwrite('data_{}.jpg'.format(time.time()), img)
print("Saving Image")

 
cap.relese()
cv.destroyAllWindows()