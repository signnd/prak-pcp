## DETEKSI TEPI SOBEL
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('gambar1_sm.jpg', cv.COLOR_BGR2GRAY)
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

grayimage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

x = cv.Sobel(grayimage, cv.CV_16S, 1, 0)
y = cv.Sobel(grayimage, cv.CV_16S, 0, 1)

absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Sobel = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

titles = ['Original image', 'Sobel operator']
images = [rgb_img, Sobel]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()