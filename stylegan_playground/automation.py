import os
import subprocess

pass_list = []  # 需要屏蔽的训练项目

if __name__ == '__main__':
    for item in os.listdir("./data"):
        if item not in pass_list:
            if item[-4:] == ".zip":
                print(item)
                # 此处采用硬地址编码，在执行前需要进一步修改
                subprocess.run(["C:\\ProgramData\\Anaconda3\\python.exe", "train.py", "--outdir=training-runs",
                                "--data=C:\\Users\\%USERNAME%\\JupyterLabProjects\\Graduation_Project\\"
                                "stylegan_playground\\data\\{}".format(item), "--gpus=1", "--metrics=none"],
                               check=True)
