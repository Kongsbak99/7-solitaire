import math
import sys

import numpy as np
import cv2
import numpy.linalg as la


class GetCardCorner:
    def GetCardCorner(self, frame):
        font = cv2.FONT_HERSHEY_COMPLEX

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Converting image to a binary image
        # ( black and white only image).
        _, threshold = cv2.threshold(imgGray, 110, 255, cv2.THRESH_BINARY)

        # Detecting contours in image.
        contours, _ = cv2.findContours(threshold, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)
        print("Number of Contours found = " + str(len(contours)))

        # The math executed if more cards are stacked which makes the card seem higher.
        def shorten(x1, x2, height, width):
            x2 = x2 - x1
            x2 = (x2 / height) * (width * 1.6)
            x2 = x2 + x1
            return x2

        def botShortenY(y1, y2, height, width):
            y2 = y2 - y1
            y2 = (y2 / height) * (width / 2.2)
            y2 = y2 + y1
            return y2

        def botShortenX(x1, x2, height, width):
            x2 = x2 - x1
            x2 = (x2 / width) * (width / 5)
            x2 = x2 + x1
            return x2

        def correctOrientation(n):  # Sets first coordinates to be top-left corner.
            # OBS: Can still be oriented wrong even if first coordinates is top-left corner
            try:
                ##corrected = [None] * 8  # empty array at fixed size
                #corrected = np.array(n)
                min_x = sys.maxsize
                min_y = sys.maxsize
                move_amount = 0

                # Find corner with lowest number (lowest should be top left corner)
                for u in range(0, len(n), 2):
                    #print("==== is " + str(n[u]) + " less than " + str(min_x))
                    print("--- " + str(u) + " to " + str(u+1))
                    print("--- " + str(n[u]) + ", " + str(n[u+1]) + " = " + str(n[u] + n[u+1]) + "\n")
                    #if n[u] < min_x and n[u+1] < min_y:
                    if n[u] + n[u+1] < min_x + min_y:
                        min_x = n[u]
                        min_y = n[u+1]
                print("============ min-x and min-y: " + str(min_x) + ", " + str(min_y))

                # Figure out how many indexes to shift array so corner with the lowest value is top-left
                if min_x in n:
                    move_amount = np.where(n == min_x)
                    move_amount = int(move_amount[0])
                    print("indexes to move: " + str(move_amount))

                # Finally shift array left
                if move_amount != 0:
                    corrected = np.roll(n, -move_amount)
                    print("finished rotating")

                    for q in range(0, len(n), 2):
                        print(str(corrected[q]) + ", " + str(corrected[q+1]))
                    return corrected
                return n
            except:
                print("Error in correctOrientation()")
                return n

        # Going through every contours found in the image.
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
            n = approx.ravel()  # flattens array
            i = 0
            minLineSize = 100

            for j in n:
                # if n[i] < 10:
                #   break
                try:
                    linelength = round(math.sqrt(((n[i + 2] - n[i]) ** 2) + ((n[i + 3] - n[i + 1]) ** 2)), 2)

                    if linelength > minLineSize:
                        cv2.drawContours(img, [approx], 0, (0, 0, 255), 2)
                        # print("i: " + str(i))
                        print("coordinates: " + "\n" + str([approx]))  # + ", " + (n[i + 2])
                    else:
                        break  # breaks a lot
                except:
                    i = i  # Cannot be empty..

                try:
                    if linelength > minLineSize:
                        x = n[i]
                        y = n[i + 1]

                        # String containing the co-ordinates and length
                        try:
                            string = str(x) + " " + str(y) + " length= " + str(linelength)
                        except:
                            string = str(x) + " " + str(y)

                        cardCoordinates = np.float32([[n[0], n[1]], [n[2], n[3]], [n[4], n[5]], [n[6], n[7]]])
                        # ptsCut = np.float32([[0, 0], [0, 450], [300, 450], [300, 0]])
                        ptsCut = np.float32([[0, 0], [0, 450], [300, 450], [300, 0]])

                        # Find angle ([2,3] = 0-point)
                        a = np.array([n[0] - n[2], n[1] - n[3]])
                        b = np.array([n[4] - n[2], n[5] - n[3]])

                        inner = np.inner(a, b)
                        norms = la.norm(a) * la.norm(b)
                        cos = inner / norms
                        rad = np.arccos(np.clip(cos, -1.0, 1.0))
                        deg = np.rad2deg(rad)

                        n = correctOrientation(n)

                        # only if degrees are reasonable, create and show warp & place text on original image
                        if 80 < deg < 100:
                            height = round(math.sqrt(((n[0] - n[2]) ** 2) + ((n[1] - n[3]) ** 2)), 2)
                            width = round(math.sqrt(((n[6] - n[0]) ** 2) + ((n[7] - n[1]) ** 2)), 2)
                            #print(height)
                            #print(width)

                            # print("is: " + str(height) + " 1.5 times bigger than: " + str(width) + " = " + str(
                            #   width * 1.5))
                            # If cards are stacked, do some math to find only the top card.
                            if height > width * 1.5:
                                cardCoordinates = np.float32([
                                    [shorten(n[2], n[0], height, width), shorten(n[3], n[1], height, width)],
                                    [n[2], n[3]],
                                    # [shorten(n[0], n[2], height, width), shorten(n[1], n[3], height, width)],
                                    # [shorten(n[6], n[4], height, width), shorten(n[7], n[5], height, width)],
                                    [n[4], n[5]],
                                    [shorten(n[4], n[6], height, width), shorten(n[5], n[7], height, width)]

                                ])
                                print("CARDS ARE STACKED")
                                # print(str(((n[2]) / height) * (width * 1.5)) + ", " + str(((n[3]) / height) * (width * 1.5)))
                                # print(str(((n[4]) / height) * (width * 1.5)) + ", " + str(((n[5]) / height) * (width * 1.5)))
                                # print(str(n[0]) + ", " + str(n[1]))
                                # print(str(shorten(n[0], n[2], height, width)) + ", " + str(shorten(n[1], n[3], height, width)))
                                # print(str(shorten(n[6], n[4], height, width)) + ", " + str(shorten(n[7], n[5], height, width)))
                                # print(str(n[6]) + ", " + str(n[7]))
                            print(cardCoordinates)

                            # [((n[2]) / height) * (width * 1.5), (n[3] / height) * (width * 1.5)],
                            # [(n[4] / height) * (width * 1.5), (n[5] / height) * (width * 1.5)],

                            # cardCoordinates = coordinates of the cards corners in image
                            # ptsCut = Size of card we want after warp
                            M = cv2.getPerspectiveTransform(cardCoordinates, ptsCut)
                            # Applies the warp on the image
                            dst = cv2.warpPerspective(imgGray, M, (300, 450))

                            # Get the bottom left corner
                            CornerCutCoordinates = np.float32([
                                [botShortenY(n[2], n[0], height, width), botShortenY(n[3], n[1], height, width)],
                                [n[2], n[3]],
                                [botShortenX(n[2], n[4], height, width), botShortenX(n[3], n[5], height, width)],
                                [botShortenX(n[2], n[6], height, width), botShortenY(n[3], n[7], height, width)]])

                            botCut = np.float32([[0, 0], [0, 240], [120, 240], [120, 0]])  # the coordinates/size of the new image
                            botM = cv2.getPerspectiveTransform(CornerCutCoordinates, botCut)
                            botDst = cv2.warpPerspective(imgGray, botM, (120, 240))
                            cv2.imshow("card zoom", botDst)

                            # Remove noise from the image. THIS USES A LOT OF PROCESSING POWER
                            # Also works with a video stream: check out cv2.fastNlMeansDenoisingMulti()
                            #_, thresholdblackwhite = cv2.threshold(botDst, 190, 255, cv2.THRESH_BINARY)
                            #denoised = cv2.fastNlMeansDenoising(botDst, None, 7, 21)
                            #blurDenoised = cv2.GaussianBlur(botDst, (5, 5), 0)

                            #cv2.imshow("Denoised", blurDenoised)

                            #inverted = cv2.bitwise_not(blurDenoised)
                            #cv2.imshow("inverted", inverted)

                            # plt.subplot(121), plt.imshow(img), plt.title('Input')
                            # plt.subplot(122), plt.imshow(dst), plt.title('Output')
                            # plt.show()

                            cv2.putText(img, string, (x, y),
                                        font, 0.6, (184, 22, 167))
                            cv2.imshow("full card", dst)

                            # _, thresholdblackwhite = cv2.threshold(dst, 190, 255, cv2.THRESH_BINARY)
                            # denoisedblackwhite = cv2.fastNlMeansDenoising(thresholdblackwhite, None, 7, 21)
                            # cv2.imshow("black white", denoisedblackwhite)

                except:
                    print("Something went wrong")
                i = i + 1

        # Showing the final image.
        cv2.imshow('image2', img)
    cv2.destroyAllWindows()
    pass

#
#   n index:
#
#   0,1     6,7
#
#
#
#   2,3     4,5
#
