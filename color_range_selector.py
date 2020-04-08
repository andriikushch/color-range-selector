import sys
import cv2
import numpy as np

colorSpaces = {
    'lab': (cv2.COLOR_BGR2LAB, 'L', 'A', 'B'),
    'rgb': (cv2.COLOR_BGR2RGB, 'R', 'G', 'B'),
    'hsv': (cv2.COLOR_BGR2HSV, 'H', 'S', 'V'),
}

if len(sys.argv) != 3:
    print("wrong parameters number")
    sys.exit()

colorSpace = sys.argv[1]
imgPath = sys.argv[2]

colorSpaceParams = None

try:
    colorSpaceParams = colorSpaces[colorSpace]
except KeyError:
    print("color space : \"{}\" not supported. Use one of [lab, rgb, hsv]".format(colorSpace))
    sys.exit()

img = cv2.imread(imgPath, cv2.IMREAD_COLOR)

if img is None:
    print("can't load image \"{}\"".format(imgPath))
    sys.exit()

cvtImage = cv2.cvtColor(img, colorSpaceParams[0])

cv2.namedWindow('image')


def update(_):
    _img = np.copy(img)

    l1 = cv2.getTrackbarPos('{} low'.format(colorSpaceParams[1]), 'image')
    l2 = cv2.getTrackbarPos('{} low'.format(colorSpaceParams[2]), 'image')
    l3 = cv2.getTrackbarPos('{} low'.format(colorSpaceParams[3]), 'image')

    h1 = cv2.getTrackbarPos('{} high'.format(colorSpaceParams[1]), 'image')
    h2 = cv2.getTrackbarPos('{} high'.format(colorSpaceParams[2]), 'image')
    h3 = cv2.getTrackbarPos('{} high'.format(colorSpaceParams[3]), 'image')

    lower_border = np.array([l1, l2, l3])
    upper_border = np.array([h1, h2, h3])

    mask = cv2.inRange(cvtImage, lower_border, upper_border)
    cv2.imshow('image', cv2.bitwise_and(_img, _img, mask=mask))

    print("Lower border : ", lower_border)
    print("Upper border : ", upper_border)


cv2.createTrackbar('{} low'.format(colorSpaceParams[1]), 'image', 0, 255, update)
cv2.createTrackbar('{} low'.format(colorSpaceParams[2]), 'image', 0, 255, update)
cv2.createTrackbar('{} low'.format(colorSpaceParams[3]), 'image', 0, 255, update)

cv2.createTrackbar('{} high'.format(colorSpaceParams[1]), 'image', 255, 255, update)
cv2.createTrackbar('{} high'.format(colorSpaceParams[2]), 'image', 255, 255, update)
cv2.createTrackbar('{} high'.format(colorSpaceParams[3]), 'image', 255, 255, update)

cv2.imshow('image', img)

k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()

cv2.destroyAllWindows()
