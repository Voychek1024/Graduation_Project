import os
import joblib
import subprocess

dataset = "./data/dtd/images/"
classes = joblib.load("./models/bad_models.pkl")
print(classes.__len__())

if __name__ == '__main__':
    for directory in classes:
        print(directory)
        for file in os.listdir("./models/" + directory):
            if ".pkl" in file:
                print("matched!, using {}".format(file))
                subprocess.run(["C:\\ProgramData\\Anaconda3\\python.exe", "generate.py",
                                "--outdir=C:\\Users\\Osea\\JupyterLabProjects\\Graduation_Project\\dtd_gan\\output\\"
                                "{}".format(directory),
                                "--network=C:\\Users\\Osea\\JupyterLabProjects\\Graduation_Project\\dtd_gan\\models\\"
                                "{}\\{}".format(directory, file), "--seeds=1-1000"], check=True)
