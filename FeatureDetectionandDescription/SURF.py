# %% [markdown]
# # SURF(Speeded-Up Robust Features)
# Use Box Filter(?) to approximate LoG (SIFT uses DoG)
# ![avatar](https://docs.opencv.org/4.0.0/surf_boxfilter.jpg)
# Use wavelet response for orientation assignment
# ![avatar](https://docs.opencv.org/4.0.0/surf_orientation.jpg)
# if rotation-invariant isn't required, U-SURF that without orientation is faster
# feature descriptor is 64 dimensions, which make process faster
# Use the sign of Laplacian(trace of Hessian Matrix) to make matching faster

# %% import
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# %% SURF in OpenCV
img = cv.imread('images3/1.jpg', 0)
# Create SURF object. You can specify params here or later.
# Here I set Hessian Threshold to 400
surf = cv.xfeatures2d.SURF_create(40000)
# Find keypoints and descriptors directly
kp, des = surf.detectAndCompute(img, None)
print(len(kp))

# %% plot on image
img2 = cv.drawKeypoints(img, kp, None, (255, 0, 0), 4)
plt.imshow(img2)

# %% U-SURF
# Check upright flag, if it False, set it to True
surf.setUpright(True)
# Recompute the feature points and draw it
kp = surf.detect(img, None)
img2 = cv.drawKeypoints(img, kp, None, (255, 0, 0), 4)
plt.imshow(img2)

# %% Feature Descriptor
# Find size of descriptor
print(surf.descriptorSize())
# That means flag, "extended" is False.
# So we make it to True to get 128-dim descriptors.
surf.setExtended(True)
kp, des = surf.detectAndCompute(img, None)
print(surf.descriptorSize())
print(des.shape)
