# import required module
import os
from xml.dom import minidom
import cv2
import latihan14_fungsi 

# assign directory
directory = 'train'

data_training = []
# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if filename.endswith(".xml"):
            mydoc = minidom.parse(f)
            items = mydoc.getElementsByTagName('filename')[0]
           
            hsl = items.firstChild.data
            gambar = 'train/'+hsl
            #print(gambar)
            
            kls = mydoc.getElementsByTagName('object')
            #print(kls[0].getElementsByTagName("name")[0].firstChild.data)
            target_kelas = kls[0].getElementsByTagName("name")[0].firstChild.data

            #image = cv2.imread(gambar)
            #cv2.imshow('Gambar Asli', image)

            fitur = latihan14_fungsi.ekstrak_fitur(gambar)
            fitur.append(target_kelas)
            #print(gambar, fitur)

            data_training.append(fitur)

#hasil ekstraksi dari data train
#print(data_training)
dataset = data_training
# convert class column to integers
latihan14_fungsi.str_column_to_int(dataset, len(dataset[0])-1)

#TRAINING
# evaluate algorithm
n_folds = 5
num_neighbors = 5
scores = latihan14_fungsi.evaluate_algorithm(dataset, latihan14_fungsi.k_nearest_neighbors, n_folds, num_neighbors)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

#TESTING
#data uji dari folder test
file_uji = 'test/orange_85.jpg'
data_uji_ciri = latihan14_fungsi.ekstrak_fitur(file_uji)
label = latihan14_fungsi.predict_classification(dataset, data_uji_ciri, num_neighbors)
print('Data=%s, Predicted: %s' % (data_uji_ciri, label))
