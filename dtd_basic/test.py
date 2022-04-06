import math
import random

import matplotlib.pyplot as plt
import cv2
import imageio
from scipy import misc, ndimage
import numpy as np
from skimage import img_as_ubyte
from skimage.exposure import cumulative_distribution


def color_space_trans(_image, _para):
    _image = cv2.cvtColor(_image, cv2.COLOR_BGR2RGB)
    rows, cols = _image.shape[:2]

    if _para == 0:
        # Vignette
        X_resultant_kernel = cv2.getGaussianKernel(cols, 200)
        Y_resultant_kernel = cv2.getGaussianKernel(rows, 200)
        resultant_kernel = Y_resultant_kernel * X_resultant_kernel.T
        mask = 255 * resultant_kernel / np.linalg.norm(resultant_kernel)
        output = np.copy(_image)
        for i in range(3):
            output[:, :, i] = output[:, :, i] * mask
        return output

    else:
        # Random Color Casting
        chn = random.randint(0, 2)
        tup = cv2.split(_image)
        tup[chn] = np.array(tup[chn]) + np.minimum(255 - tup[chn], 100)
        _image = cv2.merge(tup)

        lookUpTable = np.empty((1, 256), np.uint8)
        for i in range(256):
            lookUpTable[0, i] = np.clip(pow(i / 255.0, 1.0) * 255.0, 0, 255)

        return cv2.LUT(_image, lookUpTable)


if __name__ == '__main__':
    f = cv2.imread("./data/dtd/images/banded/banded_0002.jpg")
    file_path = "./data/dtd/images/banded/"
    file_name = "test"
    f_ct = color_space_trans(f, 0)
    imageio.imsave(file_path + file_name + '_ct.png', f_ct)

    f_cc = color_space_trans(f, 1)
    imageio.imsave(file_path + file_name + '_cc.png', f_cc)

    # plt.imshow(f_ct)
    # plt.show()
