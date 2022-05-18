## MEAN & GAUSSIAN BLUR

import cv2
import numpy as np

image = cv2.imread('gambar1_sm.jpg')

# apply 3x3 mean filter on the image
kernel = np.ones((3,3),np.float32)/9 #nilai kernel (3,3) makin besar makin terang
processed_image = cv2.filter2D(image,-1,kernel)
mean_blur = cv2.blur(image,(5,5)) #nilai kernel (5,5) makin besar makin blur
gaussian_blur = cv2.GaussianBlur(image,(5,5),0)

# display image
cv2.imshow('Original Image', image)
cv2.imshow('Mean Filter Processing', processed_image)
cv2.imshow('Mean Blur', mean_blur)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.waitKey(0)