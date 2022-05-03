import os
import subprocess

pass_list = ["banded", "blotchy", "braided"]
values = ["1.0", "3.0", "5.0"]

if __name__ == '__main__':
    for item in os.listdir("./data"):
        if item in pass_list:
            for value in values:
                subprocess.run(["C:\\ProgramData\\Anaconda3\\python.exe", "cyclegan.py", "--dataset_name",
                                "{}".format(item), "--lambda_cyc", "{}".format(value)], check=True)
