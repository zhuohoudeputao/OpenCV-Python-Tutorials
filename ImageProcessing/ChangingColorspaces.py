#%% import
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%% Changing Color-space
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

#%% Object Tracking
cap = cv2.VideoCapture(0)

while True:
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 0])
    upper_blue = np.array([130, 255, 255])
    
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    cv2.namedWindow('frame', flags=cv2.WINDOW_NORMAL|cv2.WINDOW_KEEPRATIO)
    cv2.imshow('frame', np.concatenate((frame,mask,res),axis=1))
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

#%% find HSV values to track
green = np.uint8([[[0,255,0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)