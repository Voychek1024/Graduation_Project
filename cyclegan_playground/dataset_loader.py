import os
import shutil

# for directory in os.listdir("./data/dtd/images/train"):
#     print(directory)
#     if not os.path.exists("./data/" + directory + "/train"):
#         os.makedirs("./data/" + directory + "/train")
#         os.makedirs("./data/" + directory + "/train/A")
#         os.makedirs("./data/" + directory + "/train/B")
#         os.makedirs("./data/" + directory + "/test")
#         os.makedirs("./data/" + directory + "/test/A")
#         os.makedirs("./data/" + directory + "/test/B")

classes = os.listdir("./data/dtd/images/train")
for item in classes:
    for target in os.listdir(os.path.join("./data/dtd/images/train", item)):
        if not os.path.exists(os.path.join("data/" + item + "/train/A", target)):
            shutil.copyfile(os.path.join("./data/dtd/images/train/" + item, target),
                            os.path.join("data/" + item + "/train/A", target))
        if not os.path.exists(os.path.join("data/" + item + "/train/B", target)):
            shutil.copyfile(os.path.join("./data/dtd/images/train/" + item, target),
                            os.path.join("data/" + item + "/train/B", target))
    print("train: ", item)

classes_t = os.listdir("./data/dtd/images/test")
for item in classes_t:
    for target in os.listdir(os.path.join("./data/dtd/images/test", item)):
        if not os.path.exists(os.path.join("data/" + item + "/test/A", target)):
            shutil.copyfile(os.path.join("./data/dtd/images/test/" + item, target),
                            os.path.join("data/" + item + "/test/A", target))
        if not os.path.exists(os.path.join("data/" + item + "/test/B", target)):
            shutil.copyfile(os.path.join("./data/dtd/images/test/" + item, target),
                            os.path.join("data/" + item + "/test/B", target))
    print("test: ", item)
