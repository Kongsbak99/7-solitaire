import math
import numpy as np
import cv2

# TODO  Done: Roter så kort står 100% lige
#		Done: Cut kortet ud af billedet
#		Find hjørnet (eller cut direkte til hjørnet)
#		minLineSize bør være dynamisk somehow

cap = cv2.VideoCapture(0)

# Reading image
font = cv2.FONT_HERSHEY_COMPLEX
#img = cv2.imread('Images/edgedetectionRaw2.jpg', cv2.IMREAD_COLOR)

# Reading same image in gray
#imgGray = cv2.imread('Images/edgedetectionRaw2.jpg', cv2.IMREAD_GRAYSCALE)

while(1):
    _, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #COLOR_BGR2HSV
    original = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE) #IMREAD_COLOR
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #IMREAD_GRAYSCALE
    imgGray = cv2.GaussianBlur(imgGray,(5,5),0)

    #img = cv2.imread('Images/edgedetectionRaw2.jpg', cv2.IMREAD_COLOR)

    # Reading same image in gray
    #imgGray = cv2.imread('Images/edgedetectionRaw2.jpg', cv2.IMREAD_GRAYSCALE)

    # Converting image to a binary image
    # ( black and white only image).
    _, threshold = cv2.threshold(imgGray, 110, 255, cv2.THRESH_BINARY)

    # Detecting contours in image.
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

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
                    cv2.drawContours(img, [approx], 0, (0, 0, 255), 2)
                    # print("i: " + str(i))
                    #print("coordinates: " + str([approx]))  # + ", " + (n[i + 2])
                else:
                    break

            except:
                # try:
                # 	linelength = round(math.sqrt(((n[0] - n[6]) ^ 2) + ((n[1] - n[7]) ^ 2)), 2)
                # 	#print("i: " + str(i))
                # 	#print("I found: " + str(linelength))
                # except:
                i = i  # aka do nothing

            try:
                if linelength > minLineSize:
                    x = n[i]
                    y = n[i + 1]

                    # String containing the co-ordinates and length
                    try:
                        string = str(x) + " " + str(y) + " length= " + str(linelength)
                    except:
                        string = str(x) + " " + str(y)
                    cv2.putText(img, string, (x, y),
                                font, 0.6, (184, 22, 167))

                    pts1 = np.float32([[n[0], n[1]], [n[2], n[3]], [n[4], n[5]], [n[6], n[7]]])
                    ptsCut = np.float32([[0, 0], [0, 400], [300, 400], [300, 0]])

                    M = cv2.getPerspectiveTransform(pts1, ptsCut)
                    dst = cv2.warpPerspective(original, M, (300, 400))
                    # plt.subplot(121), plt.imshow(img), plt.title('Input')
                    # plt.subplot(122), plt.imshow(dst), plt.title('Output')
                    # plt.show()
                    cv2.imshow("warp", dst)
            except:
                i = i
                #print("except")
            i = i + 1

    # Showing the final image.
    cv2.imshow('image2', img)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
