#%% [markdown]
# # FAST (Features from Accelerated Segment Test)
# real-time efficiency
# ## Feature Detection using FAST
# ![avatar](https://docs.opencv.org/4.0.0/fast_speedtest.jpg)
# let the intensity of pixel p be Ip 
# the pixel p is a corner if there exists a set of n contiguous pixels in the circle (of 16 pixels) which are all brighter than Ip+t, or all darker than Ip−t
# A high-speed test was proposed to exclude a large number of non-corners
# ## Machine Learning a Corner Detector
# store the 16 pixels around the feature point as a vector
# ![avatar](https://docs.opencv.org/4.0.0/fast_eqns.jpg)
# devide vector into 3 subsets based on three states
# Define Kp to true if p is a corner and false otherwise
# Use the ID3 algorithm (decision tree classifier) to query each subset using the variable Kp for the knowledge about the true class
# ## Non-maximal Suppression
# Detecting multiple interest points in adjacent locations
# Compute a score function, V for all the detected feature points
# V is the sum of absolute difference between p and 16 surrounding pixels values
# Consider two adjacent keypoints and compute their V values
# Discard the one with lower V value
# ## Summary
# Fast but not robust, it's depend on threshold

#%% import
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#%%
img = cv.imread('images3/1.jpg',0)
# Initiate FAST object with default values
fast = cv.FastFeatureDetector_create()
# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
# Print all default params
print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
plt.imshow(img2),plt.title('fast_true'),plt.show()
# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)
print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )
img3 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
plt.imshow(img3),plt.title('fast_false'),plt.show()
