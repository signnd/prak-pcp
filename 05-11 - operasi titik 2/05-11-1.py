import cv2
import numpy as np

img = cv2.imread('gambar1_sm.jpg', 0)
cv2.imshow('Original image', img)

row, column = img.shape

img1 = np.zeros((row, column), dtype = 'uint8')

min_range = 0
max_range = 110

for i in range(row):
    for j in range(column):
        if img[i,j]>min_range and img[i,j]<max_range:
            img1[i,j] = img[i,j]
        else:
            img1[i,j] = 0

cv2.imshow('Sliced image', img1)
cv2.waitKey(0)