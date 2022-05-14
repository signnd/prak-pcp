import cv2
import numpy as np

image = cv2.imread("gambar1_sm.jpg")

image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(image_bw)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
final_img = clahe.apply(image_bw) + 60

cv2.imshow("Equalization Histogram", equalized)
cv2.imshow("Adaptive Histogram", final_img)
cv2.waitKey(0)