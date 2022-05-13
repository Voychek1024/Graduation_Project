import os

for directory in os.listdir("./output/"):
    print(directory)
    if not os.path.exists("./pruned/" + directory):
        os.makedirs("./pruned/" + directory)
