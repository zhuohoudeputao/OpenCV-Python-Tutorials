# %% import
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %% Get Started
img = cv2.imread('images/1.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 110, 240, 0)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#plt.imshow(cv2.drawContours(img, contours, -1, (0, 255, 0), 3))
cnt = contours[6]
plt.imshow(cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3))