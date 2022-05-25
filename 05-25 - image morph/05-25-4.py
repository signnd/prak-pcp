# # # CLOSING # # #
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gambar1_sm.jpg')

kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(closing),plt.title('Closing')
plt.xticks([]),plt.yticks([])
plt.show()