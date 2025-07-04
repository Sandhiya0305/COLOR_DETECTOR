import numpy as np
import cv2

def get_limits(color):

    c = np.uint8([[color]])
    hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = np.array([hsv[0][0][0] - 10, 100, 100], dtype = np.uint8)
    upperLimit = np.array([hsv[0][0][0] + 10, 255, 255], dtype = np.uint8)

    return lowerLimit, upperLimit

