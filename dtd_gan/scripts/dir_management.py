import os

for directory in os.listdir("../data/dtd/images/"):
    print(directory)
    if not os.path.exists("../pruned/" + directory):
        os.makedirs("../pruned/" + directory)
    if not os.path.exists("../output/" + directory):
        os.makedirs("../output/" + directory)

