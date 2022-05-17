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

# df_KFold = global_rand

for partition in range(4):
    global_train = pd.DataFrame({'Path': [], 'Label': []})
    global_test = pd.DataFrame({'Path': [], 'Label': []})
    for i in range(0, 47):
        category_num = df_KFold[df_KFold['Label'] == i].__len__()
        single = category_num // 4
        # print(single*partition, single*(partition + 1) - 1)
        test_partition = df_KFold[df_KFold['Label'] == i].iloc[single * partition:single * (partition + 1), :]
        df_train = df_KFold.__deepcopy__()
        train_partition = df_train.drop(test_partition.index)
        train_partition = train_partition[train_partition['Label'] == i]
        global_train = pd.concat([global_train, train_partition])
        global_test = pd.concat([global_test, test_partition])
    global_train.iloc[:, 1] = global_train.iloc[:, 1].astype(int)
    global_train.to_csv("4Fold_P{}_train.csv".format(partition), header=False, index=False, sep=",")
    global_test.iloc[:, 1] = global_test.iloc[:, 1].astype(int)
    global_test.to_csv("4Fold_P{}_test.csv".format(partition), header=False, index=False, sep=",")
