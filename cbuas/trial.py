import cv2
import numpy as np
import os
#import matplotlib.image as mpimg

def create_dataset(folder):
    images = []
    #path = "pepaya/"
    class_name = []
    for dir in os.listdir(folder):
        for file in os.listdir(os.path.join(folder,dir)):
            if any([file.endswith(x) for x in ['.jpg']]):
                image_path = os.path.join(folder,dir,file)
                image = cv2.imread(image_path)
                images.append(image)
                class_name.append(dir)
    return images,class_name

print(images)
images, class_name = create_dataset("pepaya")

#image = cv2.imread(os.listdir(os.))
#cv2.imshow('Gambar Asli', image)

#resize
#dimension = (150, 150)
#resized = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)
#cv2.imshow('Gambar Ter-resize', resized)

#convert to HSV
#image2 = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
#h,s,v = cv2.split(image2)
#cv2.imshow('HSV', image2)

#cv2.waitKey(0)

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