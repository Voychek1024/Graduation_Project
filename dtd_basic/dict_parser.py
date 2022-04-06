import os
import random

data_dir = "./data/dtd/images"
classes = os.listdir(data_dir)
print(classes.__len__())
print(os.listdir(data_dir + "/banded"))

with open("label_test.txt", 'w', newline='\n') as val_file:
    with open("label_train.txt", 'w', newline='\n') as in_file:
        for i in range(classes.__len__()):
            for item in os.listdir(data_dir + "/" + classes[i]):
                if random.randint(0, 100) > 23:
                    in_file.write(data_dir + "/" + classes[i] + "/" + item)
                    in_file.write('\t')
                    in_file.write(str(i))
                    in_file.write('\n')
                else:
                    val_file.write(data_dir + "/" + classes[i] + "/" + item)
                    val_file.write('\t')
                    val_file.write(str(i))
                    val_file.write('\n')
