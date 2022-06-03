from ImageRecognition.image import bw_filter
from edgeDetectionLive2 import GetCardCorner
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
count = 0
while (1):
    _, frame = cap.read()
    cardCorner = GetCardCorner()

    try:
        cardCornerPicture = cardCorner.GetCardCorner(frame)
        bw_filter = bw_filter(cardCornerPicture)
    except:
        print("Could not find card corner")

    key = cv2.waitKey(5)  # Scan the keystrokes
    if key == ord('q'):  # Wait for q key to capture a frame.
        cv2.imwrite("TrainingImages/frame%d.jpg" % count, cardCornerPicture)  # save frame as JPEG file
        cv2.imshow('CardCornerPicture', cardCornerPicture)  # Display the resulting frame
        count += 1
        continue

    elif key == 27:  # Wait for key ESC to break
        cv2.destroyAllWindows()
        cap.release()
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
