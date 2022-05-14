import cv2
from cv2 import waitKey

img = cv2.imread("gambar/gambar1_sm.jpg")
cv2.imshow('Gambar Asli', img)
H, W = img.shape[:2]

degree = 90
rotationMatrix = cv2.getRotationMatrix2D((W/2, H/2), degree, 1)
rot_image = cv2.warpAffine(img, rotationMatrix, (H,W))
cv2.imshow('Gambar Hasil', rot_image)
img2 = cv2.flip(img, 0)
# cv2.imshow('Asli', img)
cv2.imshow('Gambar refleksi', img2)
waitKey(0)