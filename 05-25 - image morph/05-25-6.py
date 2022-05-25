# # # THINNING # # #

import cv2
import numpy as np

# Read image
img = cv2.imread('gambar3.jpg',0)

# Threshold image
ret,img = cv2.threshold(img, 127, 255, 0)

# Step 1: Create an empty skeleton
size = np.size(img)
skel = np.zeros(img.shape[:2], np.uint8)

# Get a Cross Shaped Kernel
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

while True:
    # Step 2: Open image
    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
    # Step 3: Subtract open from the original image
    temp = cv2.subtract(img, open)
    # Step 4: Erode the original image and refine the skeleton
    eroded = cv2.erode(img, element)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()
    # Step 5, if there are no white pixels left, quit the loop
    if cv2.countNonZero(img)==0:
        break

# Display the final skeleton
cv2.imshow("Skeleton", skel)
cv2.waitKey(0)
cv2.destroyAllWindows()