import math
import random

import matplotlib.pyplot as plt
import cv2
import imageio
from scipy import misc, ndimage
import numpy as np
from skimage import img_as_ubyte
from skimage.exposure import cumulative_distribution


def mixup(_image, _shadow):
    _image = cv2.cvtColor(_image, cv2.COLOR_BGR2RGB)
    _shadow = cv2.cvtColor(_shadow, cv2.COLOR_BGR2RGB)

    ix, iy = _image.shape[:2]
    sx, sy = _shadow.shape[:2]
    x = ix if ix < sx else sx
    y = iy if iy < sy else sy
    output = cv2.addWeighted(_image[0:x, 0:y], 0.5, _shadow[0:x, 0:y], 0.5, 1)
    return output


if __name__ == '__main__':
    f = cv2.imread("./data/dtd/images/banded/banded_0019.jpg")
    f_shadow = cv2.imread("./data/dtd/images/banded/banded_0002.jpg")
    file_path = "./data/dtd/images/banded/"
    file_name = "test"
    f_mx = mixup(f, f_shadow)
    imageio.imsave(file_path + file_name + '_mx.png', f_mx)

    plt.imshow(f_mx)
    plt.show()
