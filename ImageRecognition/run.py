from edgeDetectionLive2 import GetCardCorner
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(1):
    _, frame = cap.read()
    cardCorner = GetCardCorner()
    cardCorner.GetCardCorner(frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# import cv2
# video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#
# cv2.namedWindow("Window")
#
# while True:
#     ret, frame = video_capture.read()
#     cv2.imshow("Window", frame)
#
#     #This breaks on 'q' key
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# video_capture.release()
# cv2.destroyAllWindows()