import os

# for directory in os.listdir("./data/dtd/images"):
#     print(directory)
#     if not os.path.exists("./data/dtd/images/test/" + directory):
#         os.makedirs("./data/dtd/images/test/" + directory)

import shutil

with open("label_test.txt", 'r', encoding='utf-8') as in_file:
    lines = in_file.readlines()
    for line in lines:
        file_name = line.split('\t')[0].split('/')[-1][:-4]
        file_ext = line.split('\t')[0].split('/')[-1][-4:]
        file_path = "/".join(line.split('/')[:-1]) + "/"
        try:
            shutil.move(file_path + file_name + file_ext, file_path[:-len(file_name.split('_')[0]) - 1] + "test/" +
                        file_path[-len(file_name.split('_')[0]) - 1:] + file_name + file_ext)
        except FileNotFoundError:
            continue
