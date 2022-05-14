# memanggil library opencv
from http.client import ImproperConnectionState
import importlib
import cv2
from matplotlib import pyplot as plt
from cv2 import waitKey
import numpy as np

# menyimpan gambar dengan fungsi imread dari OpenCV
img = cv2.imread("gambar1_sm.jpg")

cv2.imshow('gambar1', img)

H, W = img.shape[:2]
gray = np.zeros((H, W), np.uint8)
for i in range(H):
    for j in range(W):
        # Perhatikan format gambar B,G,R
        gray[i,j] = np.clip(0.299 * img[i, j, 2] + 0.587 * img[i, j, 1] + 0.114 * img[i, j, 0], 0, 255)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
fig = plt.figure()
fig.add_subplot(211)
plt.imshow(img2)
fig.add_subplot(212)
plt.imshow(gray)
plt.show()

waitKey(0)

print(type(img))