import numpy as np
import cv2

# %% Capture Video from Camera
# create a ViideoCapture object
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    # press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# remember to release the source
cap.release()
cv2.destroyAllWindows()

# %% Playing Video from file
cap = cv2.VideoCapture('videos/1.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# %% Saving a Video
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('videos/output.avi', fourcc, 30.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        # frame = cv2.flip(frame, 0)
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()