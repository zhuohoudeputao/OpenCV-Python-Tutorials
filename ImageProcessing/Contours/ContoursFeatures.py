# %% import
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# # See gray image as a Two-dimensional grayscale density function
# # So you can calculate its Moments to represent its features
# # There are many kind of Menment in return 'M'
# %% Contour Features
# Moments
img = cv2.imread('images/1.jpg', 0)
plt.subplot(421)
plt.imshow(img)
ret, thresh = cv2.threshold(img, 110, 240, 0)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
area = []
for i in range(list.__len__(contours)):
    cnt = contours[i]
    M = cv2.moments(cnt)
    # Contour Area
    area.append(cv2.contourArea(cnt))
area2 = np.array(area)
area2.sort()
index = area.index(area2[area2.size-1])
print(index)

cnt = contours[index]
plt.subplot(422)
plt.imshow(cv2.drawContours(img, [cnt], 0, (0, 255, 0), 2))
# Moments
M = cv2.moments(cnt)
# moment center
cx = int(M['m10']/M['m00'])
cy = int(M['m01'] / M['m00'])

# Contour area
area = cv2.contourArea(cnt)

# Contour perimeter
perimeter = cv2.arcLength(cnt, True)

# Contour Approximation
epsilon = 0.1*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
plt.subplot(423)
plt.imshow(cv2.drawContours(img, [approx], 0, (0, 255, 0), 2))

# Convex Hull
hull = cv2.convexHull(cnt)
plt.subplot(424)
plt.imshow(cv2.drawContours(img, [hull], 0, (0, 255, 0), 2))
print(cv2.isContourConvex(cnt))  # False, hhhhhhh

# Bounding Rectangle
# 1
x, y, w, h = cv2.boundingRect(cnt)
plt.subplot(425)
plt.imshow(cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2))
# 2
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
plt.subplot(426)
plt.imshow(cv2.drawContours(img, [box], 0, (0, 0, 255), 2))

# Minimal Enclosing Circle
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
plt.subplot(427)
plt.imshow(cv2.circle(img, center, radius, (0, 255, 0), 2))

# Fitting Ellipse
ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img, ellipse, (0, 255, 0), 2)

# Fitting a line
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img, (cols-1, righty), (0, lefty), (0, 255, 0), 2)


#%%
