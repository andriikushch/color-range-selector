import cv2
import numpy as np
import sys

colorSpaces = {
    'lab': (cv2.COLOR_BGR2LAB, 'L', 'A', 'B'),
    'rgb': (cv2.COLOR_BGR2RGB, 'R', 'G', 'B'),
    'hsv': (cv2.COLOR_BGR2HSV, 'H', 'S', 'V'),
}

colorSpace = sys.argv[1]
colorSpaceParams = None

try:
    colorSpaceParams = colorSpaces[colorSpace]
except KeyError:
    print("color space : {} not supported".format(colorSpace))
    sys.exit()

img = cv2.imread(sys.argv[2], cv2.IMREAD_COLOR)
cvtImage = cv2.cvtColor(img, colorSpaceParams[0])

cv2.namedWindow('image')


def update():
    _img = np.copy(img)
    # get current positions of four trackbars
    h1 = cv2.getTrackbarPos('{}1'.format(colorSpaceParams[1]), 'image')
    s1 = cv2.getTrackbarPos('{}1'.format(colorSpaceParams[2]), 'image')
    v1 = cv2.getTrackbarPos('{}1'.format(colorSpaceParams[3]), 'image')

    h2 = cv2.getTrackbarPos('{}2'.format(colorSpaceParams[1]), 'image')
    s2 = cv2.getTrackbarPos('{}2'.format(colorSpaceParams[2]), 'image')
    v2 = cv2.getTrackbarPos('{}2'.format(colorSpaceParams[3]), 'image')

    lower_border = np.array([h1, s1, v1])
    upper_border = np.array([h2, s2, v2])

    mask = cv2.inRange(cvtImage, lower_border, upper_border)
    cv2.imshow('image', cv2.bitwise_and(_img, _img, mask=mask))

    print("Lower border : ", lower_border)
    print("Upper border : ", upper_border)


# create trackbars for color change
cv2.createTrackbar('{}1'.format(colorSpaceParams[1]), 'image', 0, 255, update)
cv2.createTrackbar('{}1'.format(colorSpaceParams[2]), 'image', 0, 255, update)
cv2.createTrackbar('{}1'.format(colorSpaceParams[3]), 'image', 0, 255, update)
cv2.imshow('image', img)
cv2.createTrackbar('{}2'.format(colorSpaceParams[1]), 'image', 255, 255, update)
cv2.createTrackbar('{}2'.format(colorSpaceParams[2]), 'image', 255, 255, update)
cv2.createTrackbar('{}2'.format(colorSpaceParams[3]), 'image', 255, 255, update)

k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()

cv2.destroyAllWindows()
