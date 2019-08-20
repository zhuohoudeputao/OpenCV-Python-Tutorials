import cv2

# %% Measuring Performance with OpenCV
img1 = cv2.imread('images/1.jpg')
e1 = cv2.getTickCount()
# your code execution
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)

e2 = cv2.getTickCount()
time = (e2 - e1) / cv2.getTickFrequency()
print(time)

# %% Default Optimization in OpenCV
print(cv2.useOptimized())

# %% Measuring Performance in IPython
# run this cell in python interactive or IPython
# %timeit is a magic command provided by IPython
# more commands are profiling, line profiling, memory measurement etc
img = cv2.imread('images/1.jpg')
%timeit res = cv2.medianBlur(img, 49)


# %% Performance Optimization Techniques
# Avoid using loops in Python as far as possible, especially double/triple loops etc. They are inherently slow.
# Vectorize the algorithm/code to the maximum possible extent because Numpy and OpenCV are optimized for vector operations.
# Exploit the cache coherence.
# Never make copies of array unless it is needed. Try to use views instead. Array copying is a costly operation.
