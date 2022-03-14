import os
import random

data_dir = './data/cifar10/test'
classes = os.listdir(data_dir)
print(classes.__len__())
classes_list = os.listdir(data_dir)

with open("test.txt", 'w', newline='\n', encoding='utf-8') as in_file:
    for item in classes_list:
        for file in os.listdir(data_dir + '/' + item):
            in_file.write(data_dir + '/' + item + '/' + file)
            in_file.write('\t')
            in_file.write(str(classes_list.index(item)))
            in_file.write('\n')

