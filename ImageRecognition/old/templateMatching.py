import cv2 as cv

from ImageRecognition.old.cannyEdgeDetection import edge_detection


def template_matching(method, img, template):
    #template = cv.imread('5diamonds.png', 0)
    w, h = template.shape[::-1]
    img2 = img.copy()

    result = cv.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv.rectangle(img2, location, bottom_right, 255, 5)
    cv.imshow('Match', img2)


class templateMatchingRun():
    template = cv.imread('../Images/5diamonds.png', 0)

    cap = cv.VideoCapture(0)

    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
               'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
    #[cv.TM_CCOEFF_NORMED]

    while (1):
        _, frame = cap.read()
        #cv.imshow("original", frame)
        #img = bw_filter(frame)

        img = edge_detection(frame)

        template_matching(5, img, template)

        #multiscale(frame, template)

        #cv.imshow("combined", img)

        k = cv.waitKey(5) & 0xFF

        if k == 27:
            break
    cv.destroyAllWindows()




