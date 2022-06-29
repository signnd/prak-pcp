import cv2
import numpy as np
from random import seed
from random import randrange
from math import sqrt

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

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
        print('[%s] => %d' % (value, i))
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup

# Find the min and max values for each column
def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax

## UNFINISHED