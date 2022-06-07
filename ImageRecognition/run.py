from ImageRecognition.write_on_image import write_on_image
from edgeDetectionLive2 import GetCardCorner
import cv2
from ImageRecognition.imageSplit import navn

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
count = 0
while 1:
    _, frame = cap.read()
    listOfFrames = navn(frame)

    for i in range(0, 12):
        write_on_image(frame, i, count)

    cv2.imshow('preview', frame)

    if cv2.waitKey(1) & 0xFF == ord('r'):
        box1 = GetCardCorner(listOfFrames[8])
        box2 = GetCardCorner(listOfFrames[9])
        box3 = GetCardCorner(listOfFrames[10])
        cv2.imshow("num0", box1)
        cv2.imshow("num1", box2)
        cv2.imshow("num2", box3)

        try:
            # cardCornerPicture = GetCardCorner(frame)
            # bw_filter = bw_filter(box1)

            cv2.imwrite("TrainingImages/frame%d.jpg" % count, box2)  # save frame as JPEG file
            cv2.imshow('CardCornerPicture', box2)  # Display the resulting frame

            count += 1
            # continue
        except:
            print("Could not find card corner")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break
