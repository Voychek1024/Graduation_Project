import os
import pandas as pd

df = pd.read_csv("label_gan.txt", sep="\t", header=None)
classes = os.listdir('../dtd_comparison/data/dtd/images/train')

df_KFold = pd.DataFrame({'Path': df.iloc[:, 0],
                         'Label': df.iloc[:, 1]})

# Per Category Randomize
global_rand = pd.DataFrame({'Path': [], 'Label': []})
for i in range(0, 47):
    origin = df_KFold[df_KFold['Label'] == i][df_KFold['Path'].str.contains('{}_0'.format(classes[i]))]\
        .reset_index(drop=True)
    rand = df_KFold[df_KFold['Label'] == i][df_KFold['Path'].str.contains('seed')].sample(frac=1).reset_index(drop=True)
    category_rand = pd.concat([origin, rand])
    global_rand = pd.concat([global_rand, category_rand])
global_rand.iloc[:, 1] = global_rand.iloc[:, 1].astype(int)

df_KFold = global_rand

single_origin = 120 // 4

for partition in range(4):
    global_train = pd.DataFrame({'Path': [], 'Label': []})
    global_test = pd.DataFrame({'Path': [], 'Label': []})
    for i in range(0, 47):
        gan_num = df_KFold[df_KFold['Label'] == i].__len__() - 120
        single = gan_num // 4
        test_partition_origin = \
            df_KFold[df_KFold['Label'] == i].iloc[partition * single_origin:(partition + 1) * single_origin]
        test_partition_gan = df_KFold[df_KFold['Label'] == i].iloc[120 + partition * single:120+(partition+1)*single]
        test_partition = pd.concat([test_partition_origin, test_partition_gan])
        df_train = df_KFold.__deepcopy__()
        train_partition_origin = df_train[df_train['Label'] == i].iloc[0:120].drop(test_partition_origin.index)
        train_partition_gan = df_train[df_train['Label'] == i].iloc[120:].drop(test_partition_gan.index)
        train_partition = pd.concat([train_partition_origin, train_partition_gan])
        global_train = pd.concat([global_train, train_partition])
        global_test = pd.concat([global_test, test_partition])
    global_train.iloc[:, 1] = global_train.iloc[:, 1].astype(int)
    global_train.to_csv("4Fold_P{}_train.csv".format(partition), header=False, index=False, sep=",")
    global_test.iloc[:, 1] = global_test.iloc[:, 1].astype(int)
    global_test.to_csv("4Fold_P{}_test.csv".format(partition), header=False, index=False, sep=",")
