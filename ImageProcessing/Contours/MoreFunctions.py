# %% import
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%
img = cv2.imread('images/1.jpg', cv2.IMREAD_GRAYSCALE)
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

# %% Convexity Defects
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0, 255, 0], 2)
    cv2.circle(img, far, 5, [0, 0, 255], -1)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %% Point Polygon Test
dist = cv2.pointPolygonTest(cnt, (50, 50), True)

# %% Match Shapes
img1 = cv2.imread('images/1.jpg', 0)
img2 = cv2.imread('images/2.jpg', 0)
ret, thresh = cv2.threshold(img1, 127, 255, 0)
ret, thresh2 = cv2.threshold(img2, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt1 = contours[0]
contours, hierarchy = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]
ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
print(ret)
