import os
import math
import random

from matplotlib.image import imread
import imageio
from scipy import misc, ndimage
import numpy as np

dataset_path = "./data/dtd/images/"

def maximize_area(w, h, angle):
    if w <= 0 or h <= 0:
        return 0, 0

    width_is_longer = w >= h
    side_long, side_short = (w, h) if width_is_longer else (h, w)

    sin_a, cos_a = abs(math.sin(angle)), abs(math.cos(angle))
    if side_short <= 2. * sin_a * cos_a * side_long or abs(sin_a - cos_a) < 1e-10:
        x = 0.5 * side_short
        wr, hr = (x / sin_a, x / cos_a) if width_is_longer else (x / cos_a, x / sin_a)
    else:
        cos_2a = cos_a * cos_a - sin_a * sin_a
        wr, hr = (w * cos_a - h * sin_a) / cos_2a, (h * cos_a - w * sin_a) / cos_2a

    return int(wr), int(hr)


def geometrical_trans(_image, _para):
    lx, ly, ch = _image.shape

    # Cropping
    if _para == 0:
        crop_idx = lx if lx < ly else ly
        crop = _image[crop_idx // 4: - crop_idx // 4, crop_idx // 4: - crop_idx // 4]
        return crop

    # up <-> down flip
    elif _para == 1:
        flip = np.flipud(_image)
        return flip

    # rotation
    elif _para == 2:
        rotate_idx = random.randint(0, 180)
        rotate = ndimage.rotate(_image, rotate_idx)
        lxx, lyy = maximize_area(lx, ly, rotate_idx)
        rotate = rotate[lxx // 2: - lxx // 2, lyy // 2: - lyy // 2]
        return rotate

    else:
        return _image


if __name__ == '__main__':
    with open("label_train.txt", 'r', encoding='utf-8') as in_file:
        with open("label_train_geo.txt", 'w', encoding='utf-8', newline='\n') as out_file:
            lines = in_file.readlines()
            for line in lines:
                file_name = line.split('\t')[0].split('/')[-1][:-4]
                file_ext = line.split('\t')[0].split('/')[-1][-4:]
                file_path = "/".join(line.split('/')[:-1]) + "/"
                f = imread(file_path + file_name + file_ext)
                out_file.write(line)

                try:
                    f_c = geometrical_trans(f, 0)
                    imageio.imsave(file_path + file_name + '_c' + file_ext, f_c)
                    out_file.write(file_path + file_name + '_c' + file_ext + '\t' + line.split('\t')[1])

                    f_f = geometrical_trans(f, 1)
                    imageio.imsave(file_path + file_name + '_f' + file_ext, f_f)
                    out_file.write(file_path + file_name + '_f' + file_ext + '\t' + line.split('\t')[1])

                    f_r = geometrical_trans(f, 2)
                    imageio.imsave(file_path + file_name + '_r' + file_ext, f_r)
                    out_file.write(file_path + file_name + '_r' + file_ext + '\t' + line.split('\t')[1])
                except ValueError:
                    continue

