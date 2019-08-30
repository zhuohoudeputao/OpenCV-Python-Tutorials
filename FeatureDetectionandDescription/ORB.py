#%% [markdown]
# # Oriented FAST and Rotated BRIEF
# An efficient alternative to SIFT or SURF
# Came from "OpenCV Labs"
# ORB is basically a fusion of FAST keypoint detector and BRIEF descriptor with many modifications to enhance the performance
# First it use FAST to find keypoints, then apply Harris corner measure to find top N points among them
# It also use pyramid to produce multiscale-features
# It computes the intensity weighted centroid of the patch with located corner at center. The direction of the vector from this corner point to centroid gives the orientation
# "steer" BRIEF according to the orientation of keypoints
# BRIEF has an important property that each bit feature has a large variance and a mean near 0.5
# For descriptor matching, multi-probe LSH which improves on the traditional LSH, is used

#%% import
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#%% 
img = cv.imread('images3/1.jpg',0)
# Initiate ORB detector
orb = cv.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
plt.imshow(img2), plt.show()