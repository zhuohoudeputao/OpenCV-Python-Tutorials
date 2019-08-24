#%% [markdown]
# # '2D' means Hue & Saturation

#%% import
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
#%% plot
img = cv.imread('images2/1.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
hsv = cv.cvtColor(img,cv.COLOR_RGB2HSV)
hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(hist,interpolation = 'nearest')

#%% 
