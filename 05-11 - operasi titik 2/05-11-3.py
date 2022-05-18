import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

img = cv2.imread('gambar1_sm.jpg', 0)
cv2.imshow('Citra Asli', img)
hist_asli = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist_asli)
plt.show()

img_equal = cv2.equalizeHist(img)
cv2.imshow('Hasil Ekualisasi Citra', img_equal)
hist_hasil = cv2.calcHist([img_equal], [0], None, [256], [0,256])
plt.plot(hist_hasil)
plt.show()
cv2.waitKey(0)