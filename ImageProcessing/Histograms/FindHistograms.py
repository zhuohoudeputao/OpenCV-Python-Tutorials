# %% [markdown] Theory
# # Histogram: Another way of understanding the image
# ## pixel-values in X-axis and corresponding number of pixels in the image on Y-axis

# %% import
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# %% Find Histogram
img = cv.imread('images/1.jpg', cv.IMREAD_GRAYSCALE)
# use opencv
hist_cv = cv.calcHist([img], [0], None, [256], [0, 256])
# use numpy
hist_np, bin_edges = np.histogram(img.ravel(), 256, [0, 256])

# %%  Plotting Histograms
# use matplotlib
# Gray
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

# Color
img = cv.imread('images/1.jpg', cv.IMREAD_COLOR)
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()

# %% Application of Mask
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv.bitwise_and(img, img, mask=mask)
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv.calcHist([img], [0], None, [256], [0, 256])
hist_mask = cv.calcHist([img], [0], mask, [256], [0, 256])
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0, 256])
plt.show()


#%%
