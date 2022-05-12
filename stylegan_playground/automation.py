import os
import subprocess

pass_list = ["banded.zip", "veined.zip", "blotchy.zip", "braided.zip", "bubbly.zip",
             "bumpy.zip", "chequered.zip", "cobwebbed.zip"]

if __name__ == '__main__':
    for item in os.listdir("./data"):
        if item not in pass_list:
            if item[-4:] == ".zip":
                print(item)
                # python train.py --outdir=training-runs --data=~\data\veined.zip --gpus=1 --metrics=none --dry_run
                subprocess.run(["C:\\ProgramData\\Anaconda3\\python.exe", "train.py", "--outdir=training-runs",
                                "--data=C:\\Users\\Osea\\JupyterLabProjects\\Graduation_Project\\"
                                "stylegan_playground\\data\\{}".format(item), "--gpus=1", "--metrics=none"],
                               check=True)

