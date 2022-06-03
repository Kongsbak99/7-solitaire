from edgeDetectionLive2 import GetCardCorner
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while (1):
    _, frame = cap.read()
    cardCorner = GetCardCorner()
    CardCornerPicture = cardCorner.GetCardCorner(frame)

    count = 0
    key = cv2.waitKey(33) & 0b11111111  # Wait for q key to capture a frame.
    k = cv2.waitKey(5) & 0xFF  # Wait for key ESC to break

    if key == ord('q'):

        cv2.imwrite("TrainingImages/frame%d.jpg" % count, CardCornerPicture)  # save frame as JPEG file
        cv2.imshow('CardCornerPicture', CardCornerPicture)  # Display the resulting frame
        count += 1
        continue

    elif k == 27:
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