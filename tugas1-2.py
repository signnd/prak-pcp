import cv2
import numpy as np
from matplotlib import pyplot as plt

plat = cv2.imread('plat-no.jpeg', cv2.IMREAD_GRAYSCALE)
th, plat_th = cv2.threshold(plat, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plat_fld = plat_th.copy()
plat_fld_in = cv2.bitwise_not(plat_fld)
ply = cv2.dilate(plat_fld, np.ones((7,7)))
ply = cv2.threshold(ply, 200, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((3,3),np.uint8)
ply1 = cv2.dilate(ply, kernel,iterations = 1)
contours, h = cv2.findContours(ply1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    rect = cv2.rectangle(plat_fld, (x,y), (x+w, y+h), (0,255,0),2)
    cropped = plat_fld[y:y+h, x:x+w]
cv2.imshow('good luck', cropped)
"""h, w = plat_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
cv2.floodFill(plat_fld_in, mask, (0,0), 255)
plat_fore = plat_fld | plat_fld_in"""

cv2.imshow('Gambar Asli', plat)
cv2.imshow('Gambar Biner', plat_th)
cv2.imshow('Gambar Invert', plat_fld_in)
cv2.imshow('Hasil Proses', ply1)
#cv2.imshow('Gambar Floodfill', plat_fld)
#cv2.imshow('Foreground', plat_fore)
cv2.waitKey(0)

r = cv2.selectROI("Pilih Area Cropping", plat_fld_inv)
crop_roi = plat_fld_inv[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
cv2.imshow('Hasil Crop', crop_roi)
cv2.waitKey(0)

#ref https://catwolf.org/qs?id=e2ac8efd-a6f6-40fc-af5d-64bfa3af7230&x=y

""""kernel = np.ones((9,9),np.uint8)
opening = cv2.morphologyEx(plat_fld, cv2.MORPH_OPEN, kernel)
cnts, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:-1]
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(plat_th, (x,y), (x+w, y+h), (0,255,15), 4)
    plata = plat_fld[y:y+h, x:x+w]
    break
cv2.imshow('Contour', opening)
cv2.imshow('ROI', plata)
"""