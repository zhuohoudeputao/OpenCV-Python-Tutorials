# %% [markdown]
# # Backprojection
# ## image segmentation
# ## finding objects of interest

# %% import
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# %% in numpy
# searchImg is the image we are going to search
searchImg = cv.imread('images2/1.jpg')
searchImg_hsv = cv.cvtColor(searchImg, cv.COLOR_BGR2HSV)
# targetObject is the region we use for identifying
targetObject = searchImg[2000:2500,0:300]
targetObject_hsv = cv.cvtColor(targetObject, cv.COLOR_BGR2HSV)

#plt.subplot(121),plt.imshow(searchImg)
#plt.subplot(122), plt.imshow(targetObject)

# Find the histograms using calcHist. Can be done with np.histogram2d also
M = cv.calcHist([targetObject_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
I = cv.calcHist([searchImg_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# Calculate the 'probability model' of targetObject
# Actually it's the key process of backprojection
R = M / I
h,s,v = cv.split(searchImg_hsv)
B = R[h.ravel(),s.ravel()]
B = np.minimum(B,1)
B = B.reshape(searchImg_hsv.shape[:2])

# Use a disc kernel to convolution(But I don't know why)
# I compare the result between with and without below two lines of code
# And I find with these code, the res is more continuous
disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
cv.filter2D(B, -1, disc, B)

# normalize and get the threshold(But I don't know why)
cv.normalize(B, B, 0, 255, cv.NORM_MINMAX)
# Because RGB data is integers in [0,255]
B = np.uint8(B)
ret, thresh = cv.threshold(B, 50, 255, 0)

# Because searchImg is 3 dimension
thresh = cv.merge((thresh, thresh, thresh))
# Find interest region
res = cv.bitwise_and(searchImg, thresh)
# Add 3 pictures together
res = np.vstack((searchImg,thresh,res))
plt.imshow(res)

# %% in OpenCV
searchImg = cv.imread('images2/1.jpg')
searchImg_hsv = cv.cvtColor(searchImg, cv.COLOR_BGR2HSV)
targetObject = searchImg[2000:2500,0:300]
targetObject_hsv = cv.cvtColor(targetObject, cv.COLOR_BGR2HSV)
# calculating object histogram
roihist = cv.calcHist([targetObject_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# normalize histogram and apply backprojection
cv.normalize(roihist, roihist, 0, 255, cv.NORM_MINMAX)
dst = cv.calcBackProject([searchImg_hsv], [0, 1], roihist, [0, 180, 0, 256], 1)
# Now convolute with circular disc
disc = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
cv.filter2D(dst, -1, disc, dst)
# threshold and binary AND
ret, thresh = cv.threshold(dst, 50, 255, 0)
thresh = cv.merge((thresh, thresh, thresh))
res = cv.bitwise_and(searchImg, thresh)
res = np.vstack((searchImg, thresh, res))
plt.imshow(res)


#%%
