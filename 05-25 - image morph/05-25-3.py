# # # OPENING # # #
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gambar1_sm.jpg')

kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(opening),plt.title('Opening')
plt.xticks([]),plt.yticks([])
plt.show()