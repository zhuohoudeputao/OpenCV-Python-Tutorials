#%% [markdown] Theory
# 1. It's a multi-stage algorithm
# 2. Stages:
## 1) Noise Reduction
## 2) Finding Intensity Gradient of the Image
# $$
# Edge\_Gradient(G) = \sqrt{G_{x}^{2}+G_{y}^{2}}
# $$
# $$
# Angle(\theta) = tan^{-1}(\frac{G_{y}}{G_{x}})
# $$
## 3) Non-maximum Suppression
## 4) Hysteresis Threshold

#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('images2/3.jpg', 0)
edges = cv2.Canny(img,80,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

#%%
