import math
import random

import matplotlib.pyplot as plt
from matplotlib.image import imread
import imageio
from scipy import misc, ndimage
import numpy as np


def color_space_trans(_image, _para):
    lx, ly, ch = _image.shape

    # Cropping
    if _para == 0:
        crop_idx = lx if lx < ly else ly
        crop = _image[crop_idx // 4: - crop_idx // 4, crop_idx // 4: - crop_idx // 4]
        return crop

    return _image


if __name__ == '__main__':
    f = imread("./data/dtd/images/banded/banded_0019.jpg")
    file_path = "./data/dtd/images/banded/"
    file_name = "test"
    f_ct = color_space_trans(f, 2)
    imageio.imsave(file_path + file_name + '_r.png', f_ct)  # uses the Image module (PIL)
