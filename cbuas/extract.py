import cv2
import os
import tobe_train
import matplotlib.image as mpimg

directory = 'pepaya'

# data_training = []
for root, dir, files in os.walk(directory):
   current_directory_path = os.path.abspath(root)
   for name in files:
    name, ext = os.path.splitext(name)
    if name.endswith(".jpg"):
        current_image_path = os.path.join(current_directory_path, name)
        current_image = mpimg.imread(current_image_path)
        images.append(current_image)
    else:
        print("Nothing Found")
#print(data_training)
#dataset = data_training
# convert class column to integers
#tobe_train.str_column_to_int(dataset, len(dataset[0])-1)

#TRAINING
# evaluate algorithm
n_folds = 5
num_neighbors = 5
'''scores = tobe_train.evaluate_algorithm(dataset, tobe_train.k_nearest_neighbors, n_folds, num_neighbors)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

#TESTING
#data uji dari folder test
file_uji = 'test/orange_85.jpg'
data_uji_ciri = tobe_train.ekstrak_fitur(file_uji)
label = tobe_train.predict_classification(dataset, data_uji_ciri, num_neighbors)
print('Data=%s, Predicted: %s' % (data_uji_ciri, label))'''
