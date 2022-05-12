import os
import zipfile

def zip_dir(path_dir, output_dir):
    zip = zipfile.ZipFile(output_dir, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(path_dir):
        fpath = path.replace(path_dir, '')
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()

if __name__ == "__main__":
    for item in os.listdir("./stylegan_playground/data"):
        zip_dir(path_dir="./stylegan_playground/data" + "/" + item, output_dir="./stylegan_playground/data/" + item + ".zip")
