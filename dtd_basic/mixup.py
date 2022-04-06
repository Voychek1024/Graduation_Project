import cv2
import imageio


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
    with open("label_train.txt", 'r', encoding='utf-8') as in_file:
        with open("label_train_mixup.txt", 'w', encoding='utf-8', newline='\n') as out_file:
            lines = in_file.readlines()
            for i in range(0, len(lines), 2):
                line = lines[i]
                file_name_1 = line.split('\t')[0].split('/')[-1][:-4]
                file_ext_1 = line.split('\t')[0].split('/')[-1][-4:]
                file_path_1 = "/".join(line.split('/')[:-1]) + "/"
                f_1 = cv2.imread(file_path_1 + file_name_1 + file_ext_1)
                out_file.write(line)
                try:
                    line_2 = lines[i + 1]
                    file_name_2 = line_2.split('\t')[0].split('/')[-1][:-4]
                    file_ext_2 = line_2.split('\t')[0].split('/')[-1][-4:]
                    file_path_2 = "/".join(line_2.split('/')[:-1]) + "/"
                    f_2 = cv2.imread(file_path_2 + file_name_2 + file_ext_2)
                    out_file.write(line_2)
                    try:
                        f_mx = mixup(f_1, f_2)
                        imageio.imsave(file_path_1 + file_name_1 + '_mx' + file_ext_1, f_mx)
                        out_file.write(file_path_1 + file_name_1 + '_mx' + file_ext_1 + '\t' + line.split('\t')[1])
                    except ValueError:
                        continue
                except IndexError:
                    continue
