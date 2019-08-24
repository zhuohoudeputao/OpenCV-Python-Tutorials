#%% import
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#%%  numpy implementation
img = cv.imread('images/1.jpg', 0)
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img2 = cdf[img]
plt.imshow(img)
plt.imshow(img2)

# in opencv
img = cv.imread('images/1.jpg', 0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))  # stacking images side-by-side
plt.imshow(res)

#%% adaptive histogram equalization
img = cv.imread('images/1.jpg', 0)
# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
plt.imshow(cl1)


#%%
