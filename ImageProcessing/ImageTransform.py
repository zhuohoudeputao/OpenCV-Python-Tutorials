# %% [markdown]
# # Fourier Transform
# ## It see an image as a frequency signal image
# ## Actually it's Image gradient map

# %% import
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# %% FFT in numpy
img = cv.imread('images2/1.jpg', cv.IMREAD_GRAYSCALE)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

# low frequency content is more white
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image')
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.show()

# %% HPF & JET
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
fshift[crow - 30: crow + 31, ccol - 30: ccol + 31] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.real(img_back)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image')
plt.subplot(132), plt.imshow(img_back, cmap='gray')
plt.title('Image after HPF')
plt.subplot(133), plt.imshow(img_back)
plt.title('Result in JET')
plt.show()

# %% DFT in OpenCV
dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * \
    np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image')
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.show()

# %% HPF in OpenCV
rows, cols = img.shape
crow, ccol = rows//2, cols//2
# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image')
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('Magnitude Spectrum')
plt.show()


#%%
