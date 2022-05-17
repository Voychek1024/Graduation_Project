import os
import pandas as pd

df = pd.read_csv("label_basic.txt", sep="\t", header=None)
classes = os.listdir('./data/dtd/images')

df_KFold = pd.DataFrame({'Path': df.iloc[:, 0],
                         'Label': df.iloc[:, 1]})
# Per Category Randomize
global_rand = pd.DataFrame({'Path': [], 'Label': []})
for i in range(0, 47):
    rand = df_KFold[df_KFold['Label'] == i].sample(frac=1).reset_index(drop=True)
    global_rand = pd.concat([global_rand, rand])
global_rand.iloc[:, 1] = global_rand.iloc[:, 1].astype(int)
print(global_rand)
