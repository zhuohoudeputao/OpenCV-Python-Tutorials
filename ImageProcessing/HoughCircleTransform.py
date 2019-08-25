#%% import
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#%% Hough Transform
img = cv.imread('images3/4.jpg')
cimg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
circles = cv.HoughCircles(cimg,cv.HOUGH_GRADIENT,1,80,
                            param1=50,param2=10,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(img,(i[0],i[1]),i[2],(256,0,),2)
    # draw the center of the circle
    cv.circle(img,(i[0],i[1]),2,(0,256,0),2)
plt.imshow(img)

#%%
