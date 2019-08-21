# %% import
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %% 2D convolution
img = cv2.imread('images/1.jpg')
kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)

# %% Image Blurring
blur = cv2.blur(img, (5, 5))
gaussianBlur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# %% plot
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
