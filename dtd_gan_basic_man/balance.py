import os
import joblib
import shutil
import numpy as np

for item in os.listdir("./data/dtd/images/gan/"):
    # print(item, os.listdir("./data/dtd/images/gan/" + item).__len__())
    file_num = os.listdir("./data/dtd/images/gan/" + item).__len__()
    if file_num > 840:
        for file in os.listdir("./data/dtd/images/gan/" + item)[-(file_num-840):]:
            os.remove("./data/dtd/images/gan/{}/".format(item) + file)
    elif file_num < 840:
        print(item, (840 - file_num))
        # stds = joblib.load("../dtd_gan/stds/{}_new.stds".format(item))
        # print(stds.__len__())
        # top_idx = np.argsort(stds)[-(840 - file_num):]
        # # print(top_idx)
        # for file_idx in top_idx:
        #     # "./output/fibrous/seed{:04d}.png".format(idx + 1)
        #     file_name = "seed{:04d}.png".format(1000 + file_idx + 1)
        #     try:
        #         shutil.move("../dtd_gan/output/{}/{}".format(item, file_name),
        #                     "./data/dtd/images/gan/{}/{}".format(item, file_name))
        #     except FileNotFoundError:
        #         print("Failed!", 800 + file_idx + 1)
