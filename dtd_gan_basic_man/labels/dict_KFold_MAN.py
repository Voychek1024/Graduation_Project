import os
import pandas as pd

df_o = pd.read_csv("../labels/label_baseline.txt", sep="\t", header=None)
df_b = pd.read_csv("../labels/label_basic_man.txt", sep="\t", header=None)
df_g = pd.read_csv("../labels/label_gan_man.txt", sep="\t", header=None)
classes = os.listdir('../data/dtd/images/baseline')

df_baseline = pd.DataFrame({'Path': df_o.iloc[:, 0],
                            'Label': df_o.iloc[:, 1]})
df_basic = pd.DataFrame({'Path': df_b.iloc[:, 0],
                         'Label': df_b.iloc[:, 1]})
df_gan = pd.DataFrame({'Path': df_g.iloc[:, 0],
                       'Label': df_g.iloc[:, 1]})

# df_KFold = pd.DataFrame({'Path': [], 'Label': []})

sample_num = 30
diff_idx = "25B-75G"
gan_comp = 720 - sample_num * 8
print(sample_num * 8, gan_comp)

for partition in range(4):
    global_train = pd.DataFrame({'Path': [], 'Label': []})
    for i in range(0, 47):
        print(partition, classes[i])
        category_train = pd.DataFrame({'Path': [], 'Label': []})
        single = 30
        sample = df_baseline[df_baseline['Label'] == i].iloc[single * partition:single * (partition + 1), :]
        sample = pd.DataFrame(sample)
        train_origin = df_baseline.__deepcopy__().drop(sample.index)
        train_origin = train_origin[train_origin['Label'] == i].sample(n=sample_num).reset_index(drop=True)
        for idx, row in train_origin.iterrows():
            basic = df_basic[df_basic['Label'] == i][df_basic['Path'].str.contains(row['Path'].split("/")[-1][:-4])]
            category_train = pd.concat([category_train, basic])
        gan_compensation = df_gan[df_gan['Label'] == i].sample(n=gan_comp).reset_index(drop=True)
        category_train = pd.concat([category_train, gan_compensation])
        category_train = category_train.reset_index(drop=True)
        global_train = pd.concat([global_train, category_train])
    global_train.iloc[:, 1] = global_train.iloc[:, 1].astype(int)
    global_train = global_train.reset_index(drop=True)
    global_train.to_csv("../labels/{}/4Fold_P{}_train.csv".format(diff_idx, partition),
                        header=False, index=False, sep=",")
