import os

for directory in os.listdir("./data/dtd/images/baseline/"):
    print(directory)
    if not os.path.exists("./data/dtd/images/25B-75G/" + directory):
        os.makedirs("./data/dtd/images/25B-75G/" + directory)
