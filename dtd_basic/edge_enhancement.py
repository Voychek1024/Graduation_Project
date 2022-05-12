import cv2


def edge_enhancement(_image):
    x = cv2.Sobel(_image, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(_image, cv2.CV_16S, 0, 1)

    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)

    dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
    dst = cv2.bitwise_not(dst)

    out = cv2.addWeighted(_image, 0.5, dst, 0.5, 0)
    return out


if __name__ == '__main__':
    with open("label_origin.txt", "r", encoding="utf-8") as in_file:
        with open("label_eh.txt", "w", encoding="utf-8", newline="\n") as out_file:
            lines = in_file.readlines()
            for line in lines:
                file_name = line.split('\t')[0].split('/')[-1][:-4]
                file_ext = line.split('\t')[0].split('/')[-1][-4:]
                file_path = "/".join(line.split('/')[:-1]) + "/"
                f = cv2.imread(file_path + file_name + file_ext)
                out_file.write(line)
                try:
                    f_eh = edge_enhancement(f)
                    cv2.imwrite(file_path + file_name + '_eh' + file_ext, f_eh)
                    out_file.write(file_path + file_name + '_eh' + file_ext + '\t' + line.split('\t')[1])
                except cv2.error:
                    print("Failed")
                    continue
