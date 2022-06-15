import cv2
import numpy as np

plat = cv2.imread('plat-no.jpeg', cv2.IMREAD_GRAYSCALE)
th, plat_th = cv2.threshold(plat, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

plat_fld = plat_th.copy()
h, w = plat_fld.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
cv2.floodFill(plat_fld, mask, (0,0), 255)
plat_fld_inv = cv2.bitwise_not(plat_fld)
plat_fore = plat_th | plat_fld_inv

cv2.imshow('Gambar Asli', plat)
cv2.imshow('Gambar Biner', plat_th)
cv2.imshow('Gambar Floodfill', plat_fld)
cv2.imshow('Gambar Invert', plat_fld_inv)
cv2.imshow('Foreground', plat_fore)
cv2.waitKey(0)

r = cv2.selectROI("Pilih Area Crop", plat_fld)
crop_roi = plat_fld[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
cv2.imshow('Hasil Crop', crop_roi)
cv2.waitKey(0)

#ref https://catwolf.org/qs?id=e2ac8efd-a6f6-40fc-af5d-64bfa3af7230&x=y