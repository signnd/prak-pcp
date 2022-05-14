import cv2
import numpy as np
from cv2 import waitKey
from matplotlib import pyplot as plt

img = cv2.imread("gambar/gambar1_sm.jpg")

# histogram
#color = ('b','g','r')
#for i,col in enumerate(color):
#    histr = cv2.calcHist([img], [i], None, [256], [0,256])
#    plt.plot(histr,color = col)
#    plt.xlim(0,256)
#plt.show()

# negation
h, w = img.shape[:2]
max_intensity = 255
for i in range(h):
    for j in range(w):
        a = img.item(i, j)
        b = max_intensity - a
        img.itemset((i, j), b)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gambar Negation', img)
histr = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(histr)
plt.show()
waitKey(0)
