import random

import cv2
import numpy as np

dataset_path = "./data/dtd/images/"


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
        tup[chn] = np.array(tup[chn]) + np.minimum(255 - tup[chn], 70)
        _image = cv2.merge(tup)

        lookUpTable = np.empty((1, 256), np.uint8)
        for i in range(256):
            lookUpTable[0, i] = np.clip(pow(i / 255.0, 1.0) * 255.0, 0, 255)

        return cv2.LUT(_image, lookUpTable)


if __name__ == '__main__':
    with open("label_origin.txt", 'r', encoding='utf-8') as in_file:
        with open("label_col.txt", 'w', encoding='utf-8', newline='\n') as out_file:
            lines = in_file.readlines()
            for line in lines:
                file_name = line.split('\t')[0].split('/')[-1][:-4]
                file_ext = line.split('\t')[0].split('/')[-1][-4:]
                file_path = "/".join(line.split('/')[:-1]) + "/"
                f = cv2.imread(file_path + file_name + file_ext)
                f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
                out_file.write(line)
                try:
                    f_cv = color_space_trans(f, 0)
                    cv2.imwrite(file_path + file_name + '_cv' + file_ext, f_cv)
                    out_file.write(file_path + file_name + '_cv' + file_ext + '\t' + line.split('\t')[1])

                    f_cc = color_space_trans(f, 1)
                    cv2.imwrite(file_path + file_name + '_cc' + file_ext, f_cc)
                    out_file.write(file_path + file_name + '_cc' + file_ext + '\t' + line.split('\t')[1])
                except cv2.error:
                    print("Failed")
                    continue
