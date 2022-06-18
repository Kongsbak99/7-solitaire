import cv2

from ImageRecognition.run import runAllCards

def getCap():
	cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
	return cap

def runmycards(cap):
	return runAllCards(cap)

cap = getCap()
runmycards(cap)