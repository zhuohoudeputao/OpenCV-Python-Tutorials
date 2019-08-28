#%% [markdown]
# # SIFT(Scale-Invariant Feature Transform)
# Harris and Shi-Tomasi detector is rotation-invariant
#
# which means when the image rotated, the same corner can still be detected
#
# but when the scale of image changed, the corner may not still be a corner, it would be flat or an edge
#
# ![avatar](https://docs.opencv.org/4.0.0/sift_scale_invariant.jpg)
#
# so Harris and Shi-Tomashi detector is not scale-invariant
#
# D.Lowe came up with a new algorithm SIFT in his paper Distinctive Image Features from Scale-Invariant Keypoints
#
# There are mainly four steps in SIFT algorithm

#%% [markdown]
# ## Scale-space Extrema Detection
# ![avatar](https://docs.opencv.org/4.0.0/sift_dog.jpg)
# ![avatar](https://docs.opencv.org/4.0.0/sift_local_extrema.jpg)
# ## Keypoint Localization
# Abandon low-intensity and edge points
# ## Orientation Assignment
# Calculate the gradient magnitude and direction histogram in a neighbourhood region
# ## Keypoint Descriptor
# A 16x16 neighbourhood around the keypoint is taken. It is divided into 16 sub-blocks of 4x4 size. For each sub-block, 8 bin orientation histogram is created. So a total of 128 bin values are available.
# ## Keypoint Matching
# Abandon too-closed matching which may be caught by noise or some other reason

#%% import
import numpy as np
import cv2 as cv

#%% SIFT in OpenCV
img = cv.imread('images/1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# AttributeError: module 'cv2.cv2' has no attribute 'xfeature2D'
# reinstall opencv, opencv-contrib to version 3.4.2.16 
sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
img= cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('sift_keypoints.jpg', img)

#%%
sift = cv.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)