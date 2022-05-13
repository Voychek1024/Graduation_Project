import os
import cv2
import numpy as np
import joblib

dataset_loc = "./output/"
classes = os.listdir(dataset_loc)
print(classes.__len__())

for directory in classes:
    if os.listdir(dataset_loc + directory).__len__():
        stds = []
        for image in os.listdir(dataset_loc + directory):
            img = cv2.imread(dataset_loc + directory + "/" + image)
            stds.append(np.std(img))
        joblib.dump(stds, "./stds/{}.stds".format(directory))
        print(stds)
