import cv2
import numpy as np
import matplotlib.pyplot as plt
# %% Scaling
img = cv2.imread('images/1.jpg')
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# OR
height, width = img.shape[:2]
res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)

# %% [markdown]
# $$
# M=\begin{bmatrix}
# 1 & 0 & t_{x}
# \\
# 0 & 1 & t_{y}
# \end{bmatrix}
# $$

# %% Translation
img = cv2.imread('images/1.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

# %% [markdown]
# $$
# M=\begin{bmatrix}
# cos(\theta ) & -sin(\theta)\\
# sin(\theta) & cos(\theta)
# \end{bmatrix}
# $$
# $$
# \begin{bmatrix}
#     \alpha & \beta & (1-\alpha)\cdot center.x - \beta\cdot center.y
#     \\
#     -\beta & \alpha & \beta\cdot center.x + (1-\alpha)\cdot center.y
# \end{bmatrix}
# $$
# $$
# \alpha = scale \cdot cos\theta
# $$
# $$
# \beta = scale \cdot sin\theta
# $$
# %% Rotation
img = cv2.imread('images/1.jpg', 0)
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

# %% Affine Transformation
img = cv2.imread('images/1.jpg')
rows, cols, ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))

# %% Perspective Transformation
img = cv2.imread('images/1.jpg')
rows, cols, ch = img.shape

pts1 = np.float32([[438,128],[438,358],[770,128],[770,358]])
pts2 = np.float32([[0, 0], [0, 300], [300, 0],[300, 300]])
M=cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img, M, (300, 300))

# %% plot
plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(dst)
plt.show()
