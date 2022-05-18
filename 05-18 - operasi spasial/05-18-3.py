## HIGH PASS FILTERING
import cv2
import numpy as np
from matplotlib import pyplot as plt
from cv2 import waitKey

def highPassFiltering(img,size):
    h, w = img.shape[0:2]
    h1,w1 = int(h/2), int(w/2)
    img[h1-int(size/2):h1+int(size/2),w1-int(size/2):w1+int(size/2)] = 0
    return img

gray = cv2.imread("gambar1_sm.jpg", 1)
gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (1280, 720))

# Fourier transform
img_dft = np.fft.fft2(gray)
dft_shift = np.fft.fftshift(img_dft) # Move frequency domain from upper left to muddle

# High-pass filter
dft_shift = highPassFiltering(dft_shift, 200)
res = np.log(np.abs(dft_shift))

# Inverse fourier transform
idft_shift = np.fft.ifftshift(dft_shift) # Move the frequency domain from the middle to the upper left corner
ifimg = np.fft.ifft2(idft_shift) # Fourier library function call
ifimg = np.abs(ifimg)
cv2.imshow("ifimg", np.int8(ifimg))
cv2.imshow("gray", gray)

# Draw picture
plt.subplot(131), plt.imshow(gray, 'gray'), plt.title('Original image')
plt.axis('off')
plt.subplot(132), plt.imshow(res, 'gray'), plt.title('High-pass filter')
plt.axis('off')
plt.subplot(133), plt.imshow(np.int8(ifimg), 'gray'), plt.title('Effect after filtering')
plt.axis('off')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()