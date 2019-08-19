import numpy as np
import cv2

# %% Read an image
# Load an color image in grayscale
# First argument is the file path
# Second argument is the way to read
img = cv2.imread('images/1.jpg', cv2.IMREAD_COLOR)
# color image will be loaded in BGR mode
# But matplotlib display images in RGB mode
# do this if you want to display in matplotlib
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])
# or
cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# %% Display an image
# First argument is the window title
# Second argument is the image
imgWindow = cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyWindow(imgWindow)

# %% Write an image
# First argument is the file name
# Second argument is the image
cv2.imwrite('messigray.png', img)
