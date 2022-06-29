import cv2
import numpy as np

def extract_features(filename):
    image = cv2.imread(filename)

    #resize
    dimension = (150, 150)
    resized = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)

    #convert to HSV
    image2 = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(image2)

    #means
    hmean = np.mean(h)
    smean = np.mean(s)
    vmean = np.mean(v)

    #standard deviation
    hstd = np.std(h)
    sstd = np.std(s)
    vstd = np.std(v)

    features = [hmean,smean,vmean,hstd,sstd,vstd]
    return features