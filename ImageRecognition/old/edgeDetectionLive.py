import math
import numpy as np
import cv2
import numpy.linalg as la

cap = cv2.VideoCapture(0)

# Reading image
font = cv2.FONT_HERSHEY_COMPLEX


while(1):
    _, frame = cap.read()
    #img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #COLOR_BGR2HSV
    originalGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #IMREAD_COLOR
    #imgGray = originalGray
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #IMREAD_GRAYSCALE
    #imgGray = cv2.GaussianBlur(imgGray,(5,5),0)


    # Converting image to a binary image
    # ( black and white only image).
    _, threshold = cv2.threshold(imgGray, 160, 255, cv2.THRESH_BINARY)

    # Detecting contours in image.
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("originalll", originalGray)
    # Going through every contours found in the image.
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
        n = approx.ravel()  # flattens array
        i = 0
        minLineSize = 10

        for j in n:
            # if n[i] < 10:
            #   break
            try:
                linelength = round(math.sqrt(((n[i + 2] - n[i]) ^ 2) + ((n[i + 3] - n[i + 1]) ^ 2)), 2)

                if linelength > minLineSize:
                    cv2.drawContours(imgGray, [approx], 0, (0, 0, 255), 2)
                    # print("i: " + str(i))
                    #print("coordinates: " + str([approx]))  # + ", " + (n[i + 2])
                else:
                    break

            except:
                i = i  # aka do nothing

            try:
                if linelength > minLineSize:
                    #if len(n) == 8:
                    x = n[i]
                    y = n[i + 1]

                    # String containing the co-ordinates and length
                    try:
                        string = str(x) + " " + str(y) + " length= " + str(linelength)
                    except:
                        string = str(x) + " " + str(y)


                    pts1 = np.float32([[n[0], n[1]], [n[2], n[3]], [n[4], n[5]], [n[6], n[7]]])
                    ptsCut = np.float32([[0, 0], [0, 400], [300, 400], [300, 0]])

                    # Find angle ([2,3] = 0-point)
                    a = np.array([n[0] - n[2], n[1] - n[3]])
                    b = np.array([n[4] - n[2], n[5] - n[3]])

                    inner = np.inner(a, b)
                    norms = la.norm(a) * la.norm(b)
                    cos = inner / norms
                    rad = np.arccos(np.clip(cos, -1.0, 1.0))
                    deg = np.rad2deg(rad)

                    if deg > 80 and deg < 100:
                        M = cv2.getPerspectiveTransform(pts1, ptsCut)
                        dst = cv2.warpPerspective(originalGray, M, (300, 400))

                        cv2.putText(imgGray, string, (x, y),
                                    font, 0.6, (0, 150, 167))
                        cv2.imshow("warp", dst)
            except:
                i = i
                #print("except")
            i = i + 1

    # Showing the final image.
    cv2.imshow('image2', imgGray)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
