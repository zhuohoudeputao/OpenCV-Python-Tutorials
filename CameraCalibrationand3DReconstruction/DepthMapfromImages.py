import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgL = cv.imread('Data/images2/6.jpg',0)
imgR = cv.imread('Data/images2/7.jpg',0)
stereo = cv.StereoBM_create(numDisparities=200, blockSize=221)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()