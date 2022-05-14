import cv2
import matplotlib.pyplot as plt

# Read an image
img = cv2.imread('gambar1_sm.jpg', 1)
plt.imshow(img)
plt.show()

# Histogram plotting of original image
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histr, color = col)

    # Limit X axis to 256
    plt.xlim([0, 256])

plt.show()

# Negate the original image
img_neg = 1 - img

plt.imshow(img_neg)
plt.show()

# Histogram plotting of negative transformed image
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histr = cv2.calcHist([img_neg], [i], None, [256], [0, 256])

    plt.plot(histr, color = col)
    plt.xlim([0, 256])

plt.show()