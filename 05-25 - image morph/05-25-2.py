# # # EROSI # # #
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gambar3.jpg')
# img = cv2.imread('gambar1_sm.jpg', cv2.IMREAD_GRAYSCALE)
# th, im_th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Erosion')
plt.xticks([]),plt.yticks([])
plt.show()