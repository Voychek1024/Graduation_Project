import matplotlib.pyplot as plt
import joblib
import os
import numpy as np

for item in os.listdir("../output_analysis/stds/"):
    stds = joblib.load("../output_analysis/stds/" + item)
    names = np.linspace(1, 1000, 1000)
    plt.figure()
    plt.grid(True)
    plt.bar(names, stds)
    plt.axhline(y=max(stds), color='g', linestyle='-')
    plt.axhline(y=min(stds), color='r', linestyle='-')
    plt.axhline(y=np.mean(stds), color='y', linestyle='-')
    plt.title("{} with max: {:.3f}, min: {:.3f}, mean: {:.3f}".format(item, max(stds), min(stds), np.mean(stds)))
    plt.savefig("../output_analysis/figs/{}.png".format(item))
