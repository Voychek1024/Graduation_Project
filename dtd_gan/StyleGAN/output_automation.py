import os
import joblib
import subprocess

dataset = "../data/dtd/images/"
classes = os.listdir(dataset)
print(classes.__len__())

if __name__ == '__main__':
    for directory in classes:
        print(directory)
        for file in os.listdir("../models/" + directory):
            if ".pkl" in file:
                print("matched!, using {}".format(file))
                # 此处采用硬地址编码，在执行前需要进一步修改
                subprocess.run(["C:\\ProgramData\\Anaconda3\\python.exe", "generate.py",
                                "--outdir=C:\\Users\\%USERNAME%\\JupyterLabProjects\\"
                                "Graduation_Project\\dtd_gan\\output\\{}".format(directory),
                                "--network=C:\\Users\\%USERNAME%\\JupyterLabProjects\\"
                                "Graduation_Project\\dtd_gan\\models\\{}\\{}".format(directory, file),
                                "--seeds=1-1000"], check=True)
