import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

cv2.namedWindow('image')


def update(x):
    _img = np.copy(img)
    # get current positions of four trackbars
    h1 = cv2.getTrackbarPos('L1', 'image')
    s1 = cv2.getTrackbarPos('A1', 'image')
    v1 = cv2.getTrackbarPos('B1', 'image')

    h2 = cv2.getTrackbarPos('L2', 'image')
    s2 = cv2.getTrackbarPos('A2', 'image')
    v2 = cv2.getTrackbarPos('B2', 'image')

    lower_border = np.array([h1, s1, v1])
    upper_border = np.array([h2, s2, v2])

    mask = cv2.inRange(lab, lower_border, upper_border)
    cv2.imshow('image', cv2.bitwise_and(_img, _img, mask=mask))

    print(lower_border)
    print(upper_border)


# create trackbars for color change
cv2.createTrackbar('L1', 'image', 0, 255, update)
cv2.createTrackbar('A1', 'image', 0, 255, update)
cv2.createTrackbar('B1', 'image', 0, 255, update)
cv2.imshow('image', img)
cv2.createTrackbar('L2', 'image', 255, 255, update)
cv2.createTrackbar('A2', 'image', 255, 255, update)
cv2.createTrackbar('B2', 'image', 255, 255, update)

k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()

cv2.destroyAllWindows()
