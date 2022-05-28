## DON'T RUN THIS
## ref: https://pyimagesearch.com/2020/07/27/opencv-grabcut-foreground-segmentation-and-extraction/

import numpy as np
import cv2
import time
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default=os.path.sep.join(["images","plat.jpg"]),help="apply grabcut")
ap.add_argument("-mask", "--mask", type=str, default=os.path.sep.join(["images","plat-mask.jpeg"]),help="path to input mask")
ap.add_argument("-c", "--iter", type=int, default=10, help="# of Grabcut iterations")
args = vars(ap.parse_args())

image = cv2.imread('plat-no.jpeg')
mask = cv2.imread('plat-no.jpeg', cv2.IMREAD_GRAYSCALE)

roughOutput = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Rough Output", roughOutput)
cv2.waitKey(0)

mask[mask > 0] = cv2.GC_PR_FGD
mask[mask == 0] = cv2.GC_BGD

fgModel = np.zeros((1, 65), dtype="float")
bgModel = np.zeros((1, 65), dtype="float")

start = time.time()
# (mask, bgModel, fgModel) = cv2.grabCut(image, mask, None, bgModel, fgModel, iterCount=args["iter"], mode=cv2.GC_INIT_WITH_MASK)
end = time.time()

values = (
    ("Definite Background", cv2.GC_BGD),
    ("Probable Background", cv2.GC_PR_BGD),
    ("Definite Foreground", cv2.GC_FGD),
    ("Probable Foreground", cv2.GC_PR_FGD),
)

for (name, value) in values:
    # print("showing mask for '{}'".format(name))
    valueMask = (mask == value).astype("uint8")*255

    cv2.imshow(name, valueMask)
    cv2.waitKey(0)