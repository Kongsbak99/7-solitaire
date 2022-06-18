import cv2

from ImageRecognition.run import runAllCards

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# if cap.isOpened():
# 	print("opened")
#
# #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
# #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# #runAllCards(cap)
#
# while 1:
# 	_, frame = cap.read()
# 	cv2.imshow("aaa", frame)
# 	runAllCards(cap)
# 	if cv2.waitKey(1) & 0xFF == ord('q'):
# 		break
#
# # After the loop release the cap object
# cap.release()
# # Destroy all the windows
# cv2.destroyAllWindows()
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
runAllCards(cap)

def getCap():
	cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
	return cap

def runmycards(cap):
	return runAllCards(cap)

cap = getCap()
runmycards(cap)