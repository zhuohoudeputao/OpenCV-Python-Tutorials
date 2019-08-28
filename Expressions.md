# Image Processing in OpenCV
## Geometric Transformations of Images
### Traslation
$$
M=\begin{bmatrix}
1 & 0 & t_{x}
\\
0 & 1 & t_{y}     
\end{bmatrix}
$$

### Rotation
$$
M=\begin{bmatrix}
cos(\theta ) & -sin(\theta)\\ 
sin(\theta) & cos(\theta)
\end{bmatrix}
$$
$$
\begin{bmatrix}
    \alpha & \beta & (1-\alpha)\cdot center.x - \beta\cdot center.y
    \\
    -\beta & \alpha & \beta\cdot center.x + (1-\alpha)\cdot center.y
\end{bmatrix}
$$
$$
\alpha = scale \cdot cos\theta 
$$
$$
\beta = scale \cdot sin\theta
$$

## Image Thresholding
### Otsu's Binarization
$$
\sigma_{w}^{2}(t) = q_{1}(t)\sigma_{1}^{2}(t) + q_{2}(t)\sigma_{2}^{2}(t)
$$
$$
q_{1}(t)=\sum_{i=1}^{t}P(i) , q_{2}(t)=\sum_{i=t+1}^{I}P(i) 
$$
$$
\mu_{1}(t)=\sum_{i=1}^{t}\frac{iP(i)}{q_{1}(t)}, \mu_{2}(t)=\sum_{i=t+1}^{I}\frac{iP(i)}{q_{2}(t)}
$$
$$
\sigma_{1}^{2}(t)=\sum_{i=1}^{t}\left [ i-\mu_{1}(t) \right ]^{2}\frac{P(i)}{q_{1}(t)}, \sigma_{2}^{2}(t)=\sum_{i=t+1}^{I}\left [ i-\mu_{2}(t) \right ]^{2}\frac{P(i)}{q_{2}(t)}
$$

## Image Gradient
### Laplacian Derivatives
$$
\Delta src = \frac{\partial^{2}src}{\partial x^{2}}+\frac{\partial^{2}src}{\partial y^{2}}
$$
$$
kernel=\begin{bmatrix}
    0&1&0
    \\
    1&-4&1
    \\
    0&1&0
\end{bmatrix}
$$

## Canny Edge Detection
### Finding Intensity Gradient of the Image
$$
Edge\_Gradient(G) = \sqrt{G_{x}^{2}+G_{y}^{2}}
$$
$$
Angle(\theta) = tan^{-1}(\frac{G_{y}}{G_{x}})
$$

### Detail in using Canny edge detection 
$$
Edge\_Gradient(G) = \left| G_{x} \right| + \left| G_{y} \right|
$$

## Contour
### Contour Properties
$$
Aspect Ratio = \frac{Width}{Height}
$$
$$
Extent = \frac{Object Area}{Bounding Rectangle Area}
$$
$$
Solidity = \frac{Contour Area}{Convex Hull Area}
$$
$$
Equivalent\ Diameter = \sqrt{\frac{4\times Contour Area}{\pi}}
$$

# Feature Detection and Description
## Harris Corner Detection
$$
E(u,v) = \sum_{x,y} \underbrace{w(x,y)}_\text{window function} \, [\underbrace{I(x+u,y+v)}_\text{shifted intensity}-\underbrace{I(x,y)}_\text{intensity}]^2
$$
$$
E(u,v) \approx \begin{bmatrix} u & v \end{bmatrix} M \begin{bmatrix} u \\ v \end{bmatrix}
$$
$$
M = \sum_{x,y} w(x,y) \begin{bmatrix}I_x I_x & I_x I_y \\ I_x I_y & I_y I_y \end{bmatrix}
$$
$$
R = det(M) - k(trace(M))^2
$$
$$
R = \lambda_1 \lambda_2 - k(\lambda_1+\lambda_2)^2
$$
## Shi-TomasiCorner Detector
$$
R = min(\lambda_1, \lambda_2)
$$
