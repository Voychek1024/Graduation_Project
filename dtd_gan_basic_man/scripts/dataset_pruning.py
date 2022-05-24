import os

with open("../labels/label_origin.txt", "r", encoding="utf-8") as in_file:
    lines = in_file.readlines()
    for line in lines:
        file_path = "/".join(line.split('/')[:-1]) + "/"
        file_name = line.split('\t')[0].split('/')[-1][:-4]
        file_ext = line.split('\t')[0].split('/')[-1][-4:]
        print(file_name)
        os.remove("../data/dtd/images/gan/{}/{}".format(file_name[:-5], file_name + file_ext))
