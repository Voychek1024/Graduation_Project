import cv2
import numpy as np


def fancy_pca(_image, alpha_std=100):
    output = _image.astype(float).copy()
    img = _image / 255.0

    img_rs = img.reshape(-1, 3)

    img_centered = img_rs - np.mean(img_rs, axis=0)
    img_cov = np.cov(img_centered, rowvar=False)
    eig_vals, eig_vecs = np.linalg.eigh(img_cov)
    sort_perm = eig_vals[::-1].argsort()
    eig_vals[::-1].sort()
    eig_vecs = eig_vecs[:, sort_perm]

    m1 = np.column_stack(eig_vecs)
    m2 = np.zeros((3, 1))
    alpha = np.random.normal(0, alpha_std)
    m2[:, 0] = alpha * eig_vals[:]

    add_vec = np.matmul(m1, m2)

    for idx in range(3):
        output[..., idx] += add_vec[idx]

    output = np.clip(output, 0.0, 255.0)
    output = output.astype(np.uint8)
    return output


if __name__ == '__main__':
    with open("label_origin.txt", "r", encoding="utf-8") as in_file:
        with open("label_fp.txt", "w", encoding="utf-8", newline="\n") as out_file:
            lines = in_file.readlines()
            for line in lines:
                file_name = line.split('\t')[0].split('/')[-1][:-4]
                file_ext = line.split('\t')[0].split('/')[-1][-4:]
                file_path = "/".join(line.split('/')[:-1]) + "/"
                f = cv2.imread(file_path + file_name + file_ext)
                out_file.write(line)
                try:
                    f_fp = fancy_pca(f)
                    cv2.imwrite(file_path + file_name + '_fp' + file_ext, f_fp)
                    out_file.write(file_path + file_name + '_fp' + file_ext + '\t' + line.split('\t')[1])
                except cv2.error:
                    print("Failed")
                    continue
