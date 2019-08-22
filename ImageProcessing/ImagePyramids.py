# %% import
import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
# %% Basic Usage
img = cv2.imread('images2/2.jpg', cv2.IMREAD_COLOR)[1000:3500, 800:1600]
lower_reso = cv2.pyrDown(img)
higher_reso = cv2.pyrUp(lower_reso)
plt.subplot(131), plt.imshow(img)
plt.subplot(132), plt.imshow(lower_reso)
plt.subplot(133), plt.imshow(higher_reso)
# %% Image Blending using Pyramids
A = cv2.imread('images2/1.jpg')
B = cv2.imread('images2/3.jpg')
# generate Gaussian pyramid for A and B
GA, GB = A.copy(), B.copy()
gpA, gpB = [GA], [GB]
for i in range(6):
    GA = cv2.pyrDown(GA)
    GB = cv2.pyrDown(GB)
    gpA.append(GA)
    gpB.append(GB)
# generate Laplacian Pyramid for A and B
lpA, lpB = [gpA[5]], [gpB[5]]
for i in range(5, 0, -1):
    GEA = cv2.pyrUp(gpA[i])
    smallerShape = gpA[i-1].shape
    LA = cv2.subtract(gpA[i-1], GEA[0:smallerShape[0],0:smallerShape[1],0:smallerShape[2]])
    GEB = cv2.pyrUp(gpB[i])
    smallerShape = gpB[i-1].shape
    LB = cv2.subtract(gpB[i-1], GEB[0:smallerShape[0],0:smallerShape[1],0:smallerShape[2]])
    lpA.append(LA)
    lpB.append(LB)
# Now add left and right halves of images in each level
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:np.int(cols/2)], lb[:, np.int(cols/2):]))
    LS.append(ls)
# now reconstruct
ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv2.pyrUp(ls_)
    smallerShape = LS[i].shape
    ls_ = cv2.add(ls_[0:smallerShape[0],0:smallerShape[1],0:smallerShape[2]], LS[i])
# image with direct connecting each half
real = np.hstack((A[:, :np.int(cols/2)], B[:, np.int(cols/2):]))
cv2.imwrite('Pyramid_blending2.jpg', ls_)
cv2.imwrite('Direct_blending.jpg', real)


# %%
