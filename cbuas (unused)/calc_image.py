import cv2
import numpy as np
import os, sys
import matplotlib.image as mpimg
from PIL import Image
import glob

'''def load_images_from_folder(folder):
images = []
directory = 'pepaya'
for root, dir, files in os.walk(directory):
    current_directory_path = os.path.abspath(root)
    for f in files:
        name, ext = os.path.splitext(f)
        if ext == ".jpg":
            current_image_path = os.path.join(current_directory_path, f)
            current_image = mpimg.imread(current_image_path)
            images.append(current_image)'''

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if any([filename.endswith(x) for x in ['.jpg']]):
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
    return images

folders = ['pepaya/matang', 'pepaya/mengkal', 'pepaya/muda',]

for folder in folders:
    images = load_images_from_folder(folder)
    input = cv2.imread(images)
    cv2.imshow('image',input)

path = "pepaya/"
dirs = os.listdir(path)
# print(dirs)

#dimension = (150, 150)

#resize
#resized = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)

#convert to HSV
#image2 = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
#h,s,v = cv2.split(image2)

#means
#hmean = np.mean(h)
#smean = np.mean(s)
#vmean = np.mean(v)

#standard deviation
#hstd = np.std(h)
#sstd = np.std(s)
#vstd = np.std(v)

#features = [hmean,smean,vmean,hstd,sstd,vstd]
#print(features)
#cv2.waitKey()
#return features