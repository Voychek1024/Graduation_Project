import os
import shutil
import random

classes = os.listdir("./data/dtd/images/basic/")

for directory in classes:
    print(directory)
    rand_basic = random.sample(os.listdir("./data/dtd/images/basic/{}/".format(directory)), k=630)
    rand_gan = random.sample(os.listdir("./data/dtd/images/gan/{}/".format(directory)), k=210)
    print(len(set(rand_basic)), len(set(rand_gan)))
    for item in rand_basic:
        shutil.copy2("./data/dtd/images/basic/{}/{}".format(directory, item),
                     "./data/dtd/images/75B-25G/{}/{}".format(directory, item))
    for item in rand_gan:
        shutil.copy2("./data/dtd/images/gan/{}/{}".format(directory, item),
                     "./data/dtd/images/75B-25G/{}/{}".format(directory, item))
