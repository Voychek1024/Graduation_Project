import os

dataset = "./data/dtd/images/"
classes = os.listdir(dataset)
print(classes)

for directory in classes:
    if not os.path.exists("./output/" + directory):
        os.makedirs("./output/" + directory)
