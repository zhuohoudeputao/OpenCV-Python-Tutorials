#%% [markdown]
# # Two Type of Distortion
# ## Radial distortion: staright lines appear to be curved
# $$
# x_{distorted} = x( 1 + k_1 r^2 + k_2 r^4 + k_3 r^6) 
# \\ 
# y_{distorted} = y( 1 + k_1 r^2 + k_2 r^4 + k_3 r^6)
# $$
# ## Tangential distortion: image-taking lense is not parallel to the imaging plane
# $$
# x_{distorted} = x + [ 2p_1xy + p_2(r^2+2x^2)] 
# \\ 
# y_{distorted} = y + [ p_1(r^2+ 2y^2)+ 2p_2xy]
# $$
# ## other information we need
# intrinsic param of camera(specific to camera): focal length and optical center
# extrinsic param of camera(about rotation and translation): translate a coordinates of a 3D point to a coordinate system
# use well-defined images to find patterns   
#%% import
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import glob

#%% 
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('images4/*.jpg')
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7,6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (7, 6), corners2, ret)
        plt.imshow(img)
        plt.show()
# Calibration
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
np.savez('Data/B', mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)



# Undistortion
# refine camera matrix
img = cv.imread('images4/left12.jpg')
h,  w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
# undistort
dst = cv.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
plt.imshow(dst),plt.title('calibresult'),plt.show()


# # undistort(The second way to do that)
# mapx, mapy = cv.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)
# dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
# # crop the image
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]
# cv.imwrite('calibresult.png', dst)

# %% Re-project error
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
    mean_error += error
print( "total error: {}".format(mean_error/len(objpoints)) )