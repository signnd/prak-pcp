import cv2
import os
from xml.dom import minidom
import calc_image

directory = 'train'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        if filename.endswith(".xml"):
            mydoc = minidom.parse(f)
            items = mydoc.getElementsByTagName('filename')[0]

            itm = items.firstChild.data
            img = 'train/'+itm
            #print(gambar)

            name = mydoc.getElementsByTagName('object')
            target_class = name[0].getElementsByTagName("name")[0].firstChild.data
            #print(target_class)

            features = calc_image.extract_features(img)
            features.append(target_class)
            #print(img, target_class, features)

            data_training.append(festures)