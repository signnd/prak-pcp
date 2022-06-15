## DETEKSI TEPI LAPLACIAN
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('gambar1_sm.jpg', cv.COLOR_BGR2GRAY)
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

grayimage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

dst = cv.Laplacian(grayimage, cv.CV_16S, ksize = 3)
Laplacian = cv.convertScaleAbs(dst)

titles = ['Original image', 'Laplacian operator']
images = [rgb_img,Laplacian]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()