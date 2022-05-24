import os
import shutil

for item in os.listdir("../output/"):
    dir_list = os.listdir("../output/" + item)
    if dir_list.__len__() > 850:
        # print(os.listdir("./output/" + item)[-(dir_list.__len__() - 840):])
        print(item, os.listdir("../output/" + item)[-(dir_list.__len__() - 850):].__len__())
        # print("./output/fibrous/seed{:04d}.png".format(idx + 1), datum)
        for file in os.listdir("../output/" + item)[-(dir_list.__len__() - 850):]:
            shutil.move("../output/{}/{}".format(item, file),
                        "../pruned/{}/{}".format(item, file))
