import cv2


def navn(frame):
    # cv2.namedWindow("preview")
    # vc = cv2.VideoCapture(0)

    # if vc.isOpened():  # try to get the first frame
    # rval, frame = vc.read()
    # else:
    #    rval = False

    # while rval:
    #  cardCorner = GetCardCorner()

    # cv2.imshow("preview", frame)
    #   rval, frame = vc.read()
    #   key = cv2.waitKey(20)
   # knight = cv2.imread("KnightSpade.jpg")
    (h, w) = frame.shape[:2]

    ## Coordinates for the rectangles of field1 - field7
    (fieldX, fieldY) = (w // 7, (h // 5) + (h // 5))

    ## Coordinates for the draw-pile and the ace-piles
    (topX, topY) = (w // 5, h // 5)

    Field1 = frame[fieldY:h, 0:fieldX]
    Field2 = frame[fieldY:h, fieldX:fieldX * 2]
    Field3 = frame[fieldY:h, fieldX * 2:fieldX * 3]
    Field4 = frame[fieldY:h, fieldX * 3:fieldX * 4]
    Field5 = frame[fieldY:h, fieldX * 4:fieldX * 5]
    Field6 = frame[fieldY:h, fieldX * 5:fieldX * 6]
    Field7 = frame[fieldY:h, fieldX * 6:fieldX * 7]
    DrawField = frame[0:fieldY, 2:topX]
    AceStack1 = frame[0:fieldY, topX:topX * 2]
    AceStack2 = frame[0:fieldY, topX * 2:topX * 3]
    AceStack3 = frame[0:fieldY, topX * 3:topX * 4]
    AceStack4 = frame[0:fieldY, topX * 4:topX * 5]

    cv2.rectangle(frame, (0, fieldY), (fieldX, h), color=(0, 0, 0), thickness=2)  # field1
    cv2.rectangle(frame, (fieldX, fieldY), (fieldX * 2, h), color=(0, 0, 0), thickness=2)  # field2
    cv2.rectangle(frame, (fieldX * 2, fieldY), (fieldX * 3, h), color=(0, 0, 0), thickness=2)  # field3
    cv2.rectangle(frame, (fieldX * 3, fieldY), (fieldX * 4, h), color=(0, 0, 0), thickness=2)  # field4
    cv2.rectangle(frame, (fieldX * 4, fieldY), (fieldX * 5, h), color=(0, 0, 0), thickness=2)  # field5
    cv2.rectangle(frame, (fieldX * 5, fieldY), (fieldX * 6, h), color=(0, 0, 0), thickness=2)  # field6
    cv2.rectangle(frame, (fieldX * 6, fieldY), (fieldX * 7, h), color=(0, 0, 0), thickness=2)  # field7
    cv2.rectangle(frame, (0, 0), (topX, fieldY), color=(0, 0, 0), thickness=2)  # stack
    cv2.rectangle(frame, (topX, 0), (topX * 2, fieldY), color=(0, 0, 0), thickness=2)  # ace1
    cv2.rectangle(frame, (topX * 2, 0), (topX * 3, fieldY), color=(0, 0, 0), thickness=2)  # ace2
    cv2.rectangle(frame, (topX * 3, 0), (topX * 4, fieldY), color=(0, 0, 0), thickness=2)  # ace3
    cv2.rectangle(frame, (topX * 4, 0), (topX * 5, fieldY), color=(0, 0, 0), thickness=2)  # ace4

    list_of_frames = [Field1, Field2, Field3, Field4, Field5, Field6,
                      Field7, DrawField, AceStack1, AceStack2, AceStack3, AceStack4]
   # cv2.imshow("knight", knight)
    # cv2.imshow("Field1", Field1)
    # cv2.imshow("Field2", Field2)
    # cv2.imshow("Field3", Field3)
    # cv2.imshow("Field4", Field4)
    # cv2.imshow("Field5", Field5)
    # cv2.imshow("Field6", Field6)
    # cv2.imshow("Field7", Field7)
    # cv2.imshow("Draw", DrawField)
    # cv2.imshow("AceStacks", AceStack1)
    # cv2.imshow("AceStacks", AceStack2)
    # cv2.imshow("AceStacks", AceStack3)
    # cv2.imshow("AceStacks", AceStack4)

    return list_of_frames
