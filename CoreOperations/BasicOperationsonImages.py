import numpy as np
import cv2

# %% Accessing and Modifying pixel values
img = cv2.imread('images/1.jpg')
px = img[100, 100]
print(px)

blue = img[100, 100, 0]  # BGR
print(blue)

img[100, 100] = [255, 255, 255]
print(img[100, 100])

img.itemset((10, 10, 2), 100)
img.item(10, 10, 2)

# %% Accessing Image Properties
print(img.shape)
print(img.size)
print(img.dtype)

# %% Image ROI
# Get the position


def draw_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.putText(img, '('+str(x)+','+str(y)+')', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)


img = cv2.imread('images/1.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_position)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:  # Esc
        break
cv2.destroyAllWindows()

# Get the subimg
img = cv2.imread('images/1.jpg')
pavilion = img[128:358, 438:753]
cv2.imshow('pavilion', pavilion)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %% Splitting and Merging Image Channels
b, g, r = cv2.split(img)
img = cv2.merge(b, g, r)

b = img[:, :, 0]

# %% Making Borders for Images(Padding)
# useful in convolution!
import matplotlib.pyplot as plt

BLUE=[255,0,0]
img1 = cv2.imread('images/1.jpg')

replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231)
plt.imshow(img1, 'gray')
plt.title('ORIGINAL')
plt.subplot(232)
plt.imshow(replicate, 'gray')
plt.title('REPLICATE')
plt.subplot(233)
plt.imshow(reflect, 'gray')
plt.title('REFLECT')
plt.subplot(234)
plt.imshow(reflect101, 'gray')
plt.title('REFLECT_101')
plt.subplot(235)
plt.imshow(wrap, 'gray')
plt.title('WRAP')
plt.subplot(236)
plt.imshow(constant, 'gray')
plt.title('CONSTANT')
plt.show()

