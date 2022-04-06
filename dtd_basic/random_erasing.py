import math
import random

import cv2
import imageio
import numpy as np


def random_erasing(_image):
    _image = cv2.cvtColor(_image, cv2.COLOR_BGR2RGB)

    while True:
        Se = random.uniform(0.02, 0.4) * _image.shape[0] * _image.shape[1]
        re = random.uniform(0.3, 1 / 0.3)

        He = int(round(math.sqrt(Se * re)))
        We = int(round(math.sqrt(Se / re)))

        xe = random.randint(0, _image.shape[1])
        ye = random.randint(0, _image.shape[0])

        if xe + We <= _image.shape[1] and ye + He <= _image.shape[0]:
            _image[ye: ye + He, xe: xe + We, :] = np.random.randint(low=0, high=255, size=(He, We, _image.shape[2]))

            return _image


if __name__ == '__main__':
    with open("label_train.txt", 'r', encoding='utf-8') as in_file:
        with open("label_train_re.txt", 'w', encoding='utf-8', newline='\n') as out_file:
            lines = in_file.readlines()
            for line in lines:
                file_name = line.split('\t')[0].split('/')[-1][:-4]
                file_ext = line.split('\t')[0].split('/')[-1][-4:]
                file_path = "/".join(line.split('/')[:-1]) + "/"
                f = cv2.imread(file_path + file_name + file_ext)
                out_file.write(line)

                try:
                    f_re = random_erasing(f)
                    imageio.imsave(file_path + file_name + '_re' + file_ext, f_re)
                    out_file.write(file_path + file_name + '_re' + file_ext + '\t' + line.split('\t')[1])
                except ValueError:
                    continue
