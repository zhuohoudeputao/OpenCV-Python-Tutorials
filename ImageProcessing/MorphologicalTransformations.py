# %% import
import numpy as np
import cv2
import matplotlib.pyplot as plt

# %% Erosion
img = cv2.imread('images/j.png', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

plt.subplot(121), plt.imshow(img)
plt.subplot(122),plt.imshow(erosion)
#%% Dilation
dilation = cv2.dilate(img,kernel,iterations = 1)

plt.imshow(dilation)
#%% opening = erosion then dilation = removing noise
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
plt.imshow(opening)

#%% closing = dilation then erosion = closing small black in objects
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.imshow(closing)

#%% Morphological Gradient = the outline of 
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.imshow(gradient)

#%% Top Hat = difference of opening and img
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
plt.imshow(tophat)

#%% Black Hat = difference of closing and img
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
plt.imshow(blackhat)

#%% Get Kernel
# Rectangular Kernel
cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

# Elliptical Kernel
cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

# Cross-shaped Kernel
cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
