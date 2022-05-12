import random

import cv2
import numpy as np
from scipy import ndimage

dataset_path = "./data/dtd/images/"


def maximize_area(w, h, angle):
    angle = np.abs(angle)
    wr, hr = (w, h) if w > h else (h, w)
    beta = np.arctan2(hr, wr)
    gamma = np.pi / 2.0 - beta - np.radians(angle)
    _f = (hr / 2.0) / np.cos(gamma)
    _x = 2.0 * _f * np.cos(beta)
    _y = 2.0 * _f * np.sin(beta)
    canvas_w = wr * np.cos(np.radians(angle)) + hr * np.sin(np.radians(angle))
    canvas_h = wr * np.sin(np.radians(angle)) + hr * np.cos(np.radians(angle))

    _x = (canvas_w - _x) / 2.0
    _y = (canvas_h - _y) / 2.0

    return int(_x), int(_y)


def random_crop(_img, crop_idx=256):
    H, W, C = _img.shape
    if W - crop_idx <= 0 or H - crop_idx <= 0:
        return _img
    x1 = np.random.randint(0, W - crop_idx)
    y1 = np.random.randint(0, H - crop_idx)
    x2 = x1 + crop_idx
    y2 = y1 + crop_idx
    return _img[y1:y2, x1:x2]


def geometrical_trans(_image, _para):
    rotate_idx = 0
    lx, ly, ch = _image.shape

    # Random cropping
    if _para == 0:
        return random_crop(_image)

    # Horizontal flip
    elif _para == 1:
        flip = np.fliplr(_image)
        return flip

    # Rotation and cropping
    elif _para == 2:
        while rotate_idx == 0:
            rotate_idx = random.randint(-20, 20)
        rotate = ndimage.rotate(_image, rotate_idx, reshape=True)
        # cv2.imshow("rotate", rotate)
        lxx, lyy = maximize_area(lx, ly, rotate_idx)
        rotate = rotate[lyy:-lyy, lxx:-lxx]
        # cv2.imshow("result", rotate)
        cv2.waitKey(0)
        return rotate

    else:
        return _image


if __name__ == '__main__':
    with open("label_origin.txt", 'r', encoding='utf-8') as in_file:
        with open("label_geo.txt", 'w', encoding='utf-8', newline='\n') as out_file:
            lines = in_file.readlines()
            for line in lines:
                file_name = line.split('\t')[0].split('/')[-1][:-4]
                file_ext = line.split('\t')[0].split('/')[-1][-4:]
                file_path = "/".join(line.split('/')[:-1]) + "/"
                f = cv2.imread(file_path + file_name + file_ext)
                out_file.write(line)
                try:
                    f_c = geometrical_trans(f, 0)
                    cv2.imwrite(file_path + file_name + '_c' + file_ext, f_c)
                    out_file.write(file_path + file_name + '_c' + file_ext + '\t' + line.split('\t')[1])

                    f_f = geometrical_trans(f, 1)
                    cv2.imwrite(file_path + file_name + '_f' + file_ext, f_f)
                    out_file.write(file_path + file_name + '_f' + file_ext + '\t' + line.split('\t')[1])

                    f_r = geometrical_trans(f, 2)
                    cv2.imwrite(file_path + file_name + '_r' + file_ext, f_r)
                    out_file.write(file_path + file_name + '_r' + file_ext + '\t' + line.split('\t')[1])
                except cv2.error:
                    print("Failed")
                    continue
