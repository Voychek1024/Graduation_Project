import os
import joblib
import cv2
import numpy as np
import shutil

for item in os.listdir("./stds/"):
    stds = joblib.load("./stds/{}".format(item))
    counter = 0
    thresh = 15.0 if min(stds) < 15.0 else 17.0
    for datum in stds:
        if datum < thresh:
            counter += 1
            idx = stds.index(datum)
            # print("./output/fibrous/seed{:04d}.png".format(idx + 1), datum)
            shutil.move("./output/{}/seed{:04d}.png".format(item[:-5], idx + 1),
                        "./pruned/{}/seed{:04d}.png".format(item[:-5], idx + 1))
    print(item, counter, thresh)
