import cv2
import matplotlib.pyplot as plt

photo1 = cv2.imread("photo1_sm.jpg")

# histogram
color = ('b','g','r')
for i, col in enumerate(color):
    hist = cv2.calcHist([photo1], [i], None, [256], [0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
cv2.imshow('Foto asli',photo1)
plt.show()
cv2.waitKey(0)

# pengurangan gambar
photo2 = cv2.imread("photo2_sm.jpg")
cv2.imshow('Foto kedua',photo2)
cv2.waitKey(0)

photo_subtr = cv2.subtract(photo2, photo1)
cv2.imshow('Hasil Pengurangan Gambar', photo_subtr)
color = ('b','g','r')
for i, col in enumerate(color):
    hist = cv2.calcHist([photo_subtr], [i], None, [256], [0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)

# negation
img_gray = cv2.cvtColor(photo_subtr, cv2.COLOR_BGR2GRAY)
cv2.imshow('Hasil Grayscale', img_gray)
hist_gray = cv2.calcHist([img_gray], [0], None, [256], [0,256])
plt.plot(hist_gray)
plt.show()
cv2.waitKey(0)

h, w = img_gray.shape[:2]
max_intensity = 255
for i in range(h):
    for j in range(w):
        a = img_gray.item(i, j)
        b = max_intensity - a
        img_gray.itemset((i, j), b)

cv2.imshow('Hasil Negasi', img_gray)
hist_gray = cv2.calcHist([img_gray], [0], None, [256], [0,256])
plt.plot(hist_gray)
plt.show()
cv2.waitKey(0)

# ekualisasi
img_gray2 = cv2.cvtColor(photo_subtr, cv2.COLOR_BGR2GRAY)
img_hist2 = cv2.calcHist([img_gray2], [0], None, [256], [0,256])
cv2.imshow('Gambar Hasil Pengurangan', img_gray2)
plt.plot(img_hist2)
plt.show()
cv2.waitKey(0)
img_gray_eq = cv2.equalizeHist(img_gray2)
cv2.imshow('Hasil Ekualisasi', img_gray_eq)
eq_hist = cv2.calcHist([img_gray_eq], [0], None, [256], [0,256])
plt.plot(eq_hist)
plt.show()
cv2.waitKey(0)