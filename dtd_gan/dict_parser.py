import os
import random

data_dir = "C:\\Users\\Erusea\\JupyterLab\\Graduation_Project\\dtd_gan\\output"
classes = os.listdir(data_dir)
print(classes.__len__())
# print(os.listdir(data_dir + "/banded"))

with open("C:\\Users\\Erusea\\JupyterLab\\Graduation_Project\\dtd_gan\\label_origin.txt", 'w', newline='\n') as val_file:
    # with open("label_train.txt", 'w', newline='\n') as in_file:
    for i in range(classes.__len__()):
        if os.listdir(data_dir + "/" + classes[i]).__len__():
            for item in os.listdir(data_dir + "/" + classes[i]):
                val_file.write(data_dir + "/" + classes[i] + "/" + item)
                val_file.write('\t')
                val_file.write(str(i))
                val_file.write('\n')
