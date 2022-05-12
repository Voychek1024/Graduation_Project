import os
import math
import random

from matplotlib.image import imread
import imageio
from scipy import misc, ndimage
import numpy as np
from PIL import Image


def geometrical_trans(_image, _para):
    lx, ly  = _image.size

    # Cropping
    if _para == 0:
        crop_idx = lx if lx < ly else ly
        left = (lx - 256) /2
        top = (ly - 256)/2
        right = (lx + 256)/2
        bottom = (ly + 256)/2
        crop = _image.crop((left, top, right, bottom))
        return crop


if __name__ == "__main__":
    for item in os.listdir("./stylegan_playground/data"):
        for file in os.listdir("./stylegan_playground/data" + "/" + item):
            try:
                print(file)
                f = Image.open("./stylegan_playground/data" + "/" + item + "/" + file)
                f = geometrical_trans(f, 0)
                f = f.resize((256, 256))
                imageio.imsave("./stylegan_playground/data" + "/" + item + "/" + file[:-4] + ".png", f)
            except ValueError()():
                print("Failed!")
            os.remove("./stylegan_playground/data" + "/" + item + "/" + file[:-4] + ".jpg")
