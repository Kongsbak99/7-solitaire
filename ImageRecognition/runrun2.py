import cv2

from ImageRecognition.run import runAllCards


def getcap():
	cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
	return cap

def runme(cap):
	_, frame = cap.read()
	# cv2.imshow("aaa", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cap.release()
		# Destroy all the windows
		cv2.destroyAllWindows()
	kort = runAllCards(cap)
	print(kort[5].card)

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#
# while 1:
# 	_, frame = cap.read()
# 	#cv2.imshow("aaa", frame)
# 	if cv2.waitKey(1) & 0xFF == ord('q'):
# 		cap.release()
# 		# Destroy all the windows
# 		cv2.destroyAllWindows()
# 	kort = runAllCards(cap)
# 	print(kort[5].card)
