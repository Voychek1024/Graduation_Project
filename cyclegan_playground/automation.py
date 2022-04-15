import os
import subprocess

pass_list = ["banded", "blotchy", "braided"]

if __name__ == '__main__':
    for item in os.listdir("./data"):
        if item not in pass_list:
            subprocess.run(["C:\\ProgramData\\Anaconda3\\python.exe", "cyclegan.py", "--dataset_name",
                            "{}".format(item)], check=True)
