# %% import
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%% 
img = cv2.imread('images/1.jpg', 0)
imgray = cv2.cvtcolor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 110, 240, 0)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
area = []
for i in range(list.__len__(contours)):
    cnt = contours[i]
    area.append(cv2.contourArea(cnt))
area2 = np.array(area)
area2.sort()
index = area.index(area2[area2.size-1])
cnt = contours[index]
area = area[index]

# Aspect Ratio
x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w) / h

# Extent
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area) / rect_area

# Solidity
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area) / hull_area

# Equivalent Diameter
equi_diameter = np.sqrt(4 * area / np.pi)

# Orientation
(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)

# Mask and Pixel Points
mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv.findNonZero(mask)

# Maximum Value, Minimum Value and their locations
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray, mask=mask)

# Mean Color or Mean Intensity
mean_val = cv2.mean(img, mask=mask)

# Extreme Points
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
