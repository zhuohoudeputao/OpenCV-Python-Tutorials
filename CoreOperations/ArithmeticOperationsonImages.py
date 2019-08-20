import numpy as np
import cv2

# %% Image Addition
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))  # 250+10=260=>255
print(x + y)  # 250+10=260%256=4


# %% Image Blending
img1 = cv2.imread('images/1.jpg')
img2 = cv2.imread('images/2.jpg')

dst = cv2.addWeighted(img1[0:200, 0:200], 0.7, img2[0:200, 0:200], 0.3, 0)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %% Bitwise Operations
# use color image1 will get an outstanding effect
img1 = cv2.imread('images/1.jpg')[0:200, 0:200]
img2 = cv2.imread('images/2.jpg')[0:200, 0:200]

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img1.shape
roi = img2[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img1gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

img1_fg = cv2.bitwise_and(img1, img1, mask=mask)

dst = cv2.add(img2_bg, img1_fg)
img2[0:rows, 0:cols] = dst
cv2.imshow('res', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# %% slide show of images
img1_index = 1
img2_index = 2
alpha = 1
endpoint = 7 # Because I have 7 images for now
while True:
    img1 = cv2.imread('images/' + str(img1_index) + '.jpg')[0:200, 0:200]
    img2 = cv2.imread('images/' + str(img2_index) + '.jpg')[0:200, 0:200]
    while alpha > 0 & img2_index <= endpoint:
        res = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)
        cv2.imshow('res', res)
        cv2.waitKey(100)
        alpha -= 0.1
    img1_index += 1
    img2_index += 1
    alpha = 1
    if img2_index > endpoint:
        break
cv2.destroyAllWindows()
