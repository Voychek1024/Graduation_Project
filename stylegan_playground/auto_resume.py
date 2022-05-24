import joblib
import os
import subprocess

bad = joblib.load("bad_models.pkl")
print(bad.__len__())

if __name__ == '__main__':
    for item in bad:
        for directory in os.listdir("./training-runs/"):
            if item in directory and "resumecustom" not in directory:
                print(directory)
                # 此处采用硬地址编码，在执行前需要进一步修改，对模型追加100kimg训练
                subprocess.run(["C:\\ProgramData\\Anaconda3\\python.exe", "train.py", "--outdir=training-runs",
                                "--data=C:\\Users\\%USERNAME%\\JupyterLabProjects\\Graduation_Project\\"
                                "stylegan_playground\\data\\{}.zip".format(item),
                                "--resume=C:\\Users\\%USERNAME%\\JupyterLabProjects\\Graduation_Project\\"
                                "stylegan_playground\\training-runs\\{}\\network-snapshot-000200.pkl".format(directory),
                                "--gpus=1", "--metrics=none"],
                               check=True)
