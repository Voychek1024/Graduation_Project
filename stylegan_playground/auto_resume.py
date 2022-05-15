import joblib
import os
import subprocess

bad = joblib.load("bad_models.pkl")
print(bad.__len__())

if __name__ == '__main__':
    for item in bad[-7:]:
        if item == "marbled":
            break
        for directory in os.listdir("./training-runs/"):
            if item in directory and "resumecustom" not in directory:
                print(directory)
                subprocess.run(["C:\\ProgramData\\Anaconda3\\python.exe", "train.py", "--outdir=training-runs",
                                "--data=C:\\Users\\Osea\\JupyterLabProjects\\Graduation_Project\\"
                                "stylegan_playground\\data\\{}.zip".format(item),
                                "--resume=C:\\Users\\Osea\\JupyterLabProjects\\Graduation_Project\\"
                                "stylegan_playground\\training-runs\\{}\\network-snapshot-000200.pkl".format(directory),
                                "--gpus=1", "--metrics=none"],
                               check=True)
