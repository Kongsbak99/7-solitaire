import math
import sys
import numpy as np
import cv2
import numpy.linalg as la


def GetCardCorner(frame):
    font = cv2.FONT_HERSHEY_COMPLEX

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    minLineSize = 70

    # Converting image to a binary image
    # ( black and white only image).
    blur = cv2.blur(imgGray, (5, 5))
    _, threshold = cv2.threshold(blur, 130, 255, cv2.THRESH_BINARY)
    # Detecting contours in image.
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # print("Number of Contours found = " + str(len(contours)))

    # The math executed if more cards are stacked which makes the card seem higher.
    def shorten(x1, x2, height, width):
        x2 = x2 - x1
        x2 = (x2 / height) * (width * 1.4)
        x2 = x2 + x1
        return x2

    def botShortenY(y1, y2, height, width):
        y2 = y2 - y1
        y2 = (y2 / height) * (width / 0.9)  # 1.4
        y2 = y2 + y1
        return y2

    def botShortenX(x1, x2, height, width):
        x2 = x2 - x1
        x2 = (x2 / width) * (width / 1.5)  # 3
        x2 = x2 + x1
        return x2

    def correctOrientation(n):  # Sets first coordinates to be top-left corner.
        # OBS: Can still be oriented wrong even if first coordinates is top-left corner
        try:
            min_x = sys.maxsize
            min_y = sys.maxsize
            move_amount = 0

            # Find corner with lowest number (lowest should be top left corner)
            for u in range(0, len(n), 2):
                if n[u] + n[u + 1] < min_x + min_y:
                    min_x = n[u]
                    min_y = n[u + 1]
            # print("============ min-x and min-y: " + str(min_x) + ", " + str(min_y))

            # Figure out how many indexes to shift array so corner with the lowest value is top-left
            if min_x in n:
                move_amount = np.where(n == min_x)
                move_amount = int(move_amount[0])
                # print("indexes to move: " + str(move_amount))

            # Finally shift array left
            if move_amount != 0:
                corrected = np.roll(n, -move_amount)
                # print("finished rotating")
                return corrected
            return n
        except:
            # print("Error in correctOrientation()")
            return n

    # removes vectors with odd angles if there's 5 or 6 vectors.
    def get4vectors(n):
        v1 = [n[0], n[1]]
        v2 = [n[2], n[3]]
        v3 = [n[4], n[5]]
        v4 = [n[6], n[7]]
        v5 = [n[8], n[9]]
        v6 = None
        if len(n) > 11:
            v6 = [n[10], n[11]]

        # origin 0,0
        a = np.array([v5[0] - v1[0], v5[1] - v1[1]])
        b = np.array([v2[0] - v1[0], v2[1] - v1[1]])
        deg1 = calcAngle(a, b)

        # origin 2,3
        a = np.array([v1[0] - v2[0], v1[1] - v2[1]])
        b = np.array([v3[0] - v2[0], v3[1] - v2[1]])
        deg2 = calcAngle(a, b)

        # origin 4,5
        a = np.array([v2[0] - v3[0], v2[1] - v3[1]])
        b = np.array([v4[0] - v3[0], v4[1] - v3[1]])
        deg3 = calcAngle(a, b)

        # origin 6,7
        a = np.array([v3[0] - v4[0], v3[1] - v4[1]])
        b = np.array([v5[0] - v4[0], v5[1] - v4[1]])
        deg4 = calcAngle(a, b)

        if v6 is not None:
            # origin 8,9
            a = np.array([v4[0] - v5[0], v4[1] - v5[1]])
            b = np.array([v6[0] - v5[0], v6[1] - v5[1]])
            deg5 = calcAngle(a, b)

            # origin 10,11
            a = np.array([v5[0] - v6[0], v5[1] - v6[1]])
            b = np.array([v1[0] - v6[0], v1[1] - v6[1]])
            deg6 = calcAngle(a, b)

            if deg6 > 100:
                n = np.delete(n, [10, 11])
        else:
            # origin 8,9
            a = np.array([v4[0] - v5[0], v4[1] - v5[1]])
            b = np.array([v1[0] - v5[0], v1[1] - v5[1]])
            deg5 = calcAngle(a, b)

        if deg1 > 100:
            n = np.delete(n, [0, 1])
        elif deg2 > 100:
            n = np.delete(n, [2, 3])
        elif deg3 > 100:
            n = np.delete(n, [4, 5])
        elif deg4 > 100:
            n = np.delete(n, [6, 7])
        elif deg5 > 100:
            n = np.delete(n, [8, 9])

        # print("finished")
        return n

    def calcAngle(a, b):
        inner = np.inner(a, b)
        norms = la.norm(a) * la.norm(b)
        cos = inner / norms
        rad = np.arccos(np.clip(cos, -1.0, 1.0))
        deg = np.rad2deg(rad)
        return deg

    # Going through every contours found in the image.
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
        n = approx.ravel()  # flattens array
        i = 0

        for j in n:
            try:
                linelength = round(math.sqrt(((n[i + 2] - n[i]) ** 2) + ((n[i + 3] - n[i + 1]) ** 2)), 2)
                if linelength > minLineSize:
                    x = n[i]
                    y = n[i + 1]

                    # String containing the co-ordinates and length
                    try:
                        string = str(x) + " " + str(y) + " length= " + str(linelength)
                    except:
                        string = str(x) + " " + str(y)

                    # if 5 vectors, remove the one with an odd angle
                    if 13 > len(n) > 8:
                        n = get4vectors(n)

                    # Find angle ([2,3] = 0-point)
                    a = np.array([n[0] - n[2], n[1] - n[3]])
                    b = np.array([n[4] - n[2], n[5] - n[3]])
                    deg = calcAngle(a, b)

                    n = correctOrientation(n)
                    cardCoordinates = np.float32([[n[0], n[1]], [n[2], n[3]], [n[4], n[5]], [n[6], n[7]]])

                    # only if degrees are reasonable, create and show warp & place text on original image
                    if 80 < deg < 100:
                        height = round(math.sqrt(((n[0] - n[2]) ** 2) + ((n[1] - n[3]) ** 2)), 2)
                        width = round(math.sqrt(((n[6] - n[0]) ** 2) + ((n[7] - n[1]) ** 2)), 2)

                        # If cards are stacked, do some math to find only the top card.
                        n[0] = shorten(n[2], n[0], height, width)
                        n[1] = shorten(n[3], n[1], height, width)

                        n[6] = shorten(n[4], n[6], height, width)
                        n[7] = shorten(n[5], n[7], height, width)

                        if height > width * 1.5:
                            # print("CARDS ARE STACKED")
                            cardCoordinates = np.float32([
                                [n[0], n[1]],
                                [n[2], n[3]],
                                [n[4], n[5]],
                                [n[6], n[7]]
                            ])
                            # print(cardCoordinates)

                        # cardCoordinates = coordinates of the cards corners in image
                        # ptsCut = Size of card we want after warp
                        ptsCut = np.float32([[0, 0], [0, 420], [300, 420], [300, 0]])
                        M = cv2.getPerspectiveTransform(cardCoordinates, ptsCut)
                        # Applies the warp on the image
                        dst = cv2.warpPerspective(imgGray, M, (300, 420))

                        # Height and width of our cards
                        height = 8.8
                        width = 6.3
                        CornerCutCoordinates = np.float32([
                            [0, 0],
                            [0, botShortenY(0, 420, height, width)],
                            [botShortenX(0, 300, height, width), botShortenY(0, 420, height, width)],
                            [botShortenX(0, 300, height, width), 0]])

                        botCut = np.float32(
                            [[0, 0], [0, 250], [150, 250], [150, 0]])  # the coordinates/size of the new image
                        botM = cv2.getPerspectiveTransform(CornerCutCoordinates, botCut)  # 120, 257
                        botDst = cv2.warpPerspective(dst, botM, (150, 250))  # imgGray

                        cv2.putText(img, string, (x, y),
                                    font, 0.6, (184, 22, 167))
                        # cv2.imshow("full card", dst)

                        return botDst

            except:
                i = i
            i = i + 1

    # Showing the final image.
    return frame


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
