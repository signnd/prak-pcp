import cv2
import numpy as np
from cv2 import waitKey

image = cv2.imread('train/apple_1.jpg')
cv2.imshow('Gambar Asli', image)

#resize
dimension = (150, 150)
resized = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)
cv2.imshow('Gambar Ter-resize', resized)

#convert to HSV
image2 = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(image2)
cv2.imshow('HSV', image2)

cv2.waitKey(0)

#means
hmean = np.mean(h)
smean = np.mean(s)
vmean = np.mean(v)

#standard deviation
hstd = np.std(h)
sstd = np.std(s)
vstd = np.std(v)

features = [hmean,smean,vmean,hstd,sstd,vstd]
print(features)