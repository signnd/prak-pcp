# # # REGION FILLING # # #
import cv2
import numpy as np

# Read image
im_th = cv2.imread('gambar3.jpg')

im_floodfill = im_th.copy()

# Mask used to flood filling
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255)

# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)

# Combine the two images to get the foreground
im_out = im_th | im_floodfill_inv

cv2.imshow("Thresholded Image", im_th)
cv2.waitKey(0)
cv2.imshow("Floodfilled Image", im_floodfill)
cv2.waitKey(0)
cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
cv2.waitKey(0)
cv2.imshow("Foreground", im_out)
cv2.waitKey(0)


