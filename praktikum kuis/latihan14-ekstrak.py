import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('train/apple_1.jpg')
cv2.imshow('Gambar Asli', image)

# resize image
width = 150
height = 150
dim = (width, height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('Gambar Resize', resized)

image2 = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
cv2.imshow('Gambar HSV', image2)

h, s, v = cv2.split(image2)
#hsv2 = cv2.merge([h,s,v])

hmean = np.mean(h)
smean = np.mean(s)
vmean = np.mean(v)

# compute std of each channel
hstd = np.std(h)
sstd = np.std(s)
vstd = np.std(v)

# print results
#print("mean:", hmean,smean,vmean)
#print("std:", hstd,sstd,vstd)

fitur = [hmean,smean,vmean,hstd,sstd,vstd]
print(fitur)
cv2.waitKey()
