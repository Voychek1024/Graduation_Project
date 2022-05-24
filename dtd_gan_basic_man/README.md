#### 复合增强方法组
任务概述：按照25%为步长，混合基本变换、深度学习数据集

| 数据集  | 原始数据(每类) | 基本变换(每类) | 深度学习(每类) | 类内总量@类间比例 |
| ------- | -------------- | -------------- | -------------- | ----------------- |
| 75B-25G | 120            | 630            | 210            | 960 @ 2.13%       |
| 50B-50G | 120            | 420            | 420            | 960 @ 2.13%       |
| 25B-75G | 120            | 210            | 630            | 960 @ 2.13%       |

在复合增强方法增强后的数据集上，使用ResNet50模型，训练、测试，以及收集结果

#### 目录结构：

| 相对路径                                                     | 描述                                                        |
| ------------------------------------------------------------ | :---------------------------------------------------------- |
| &ensp;&ensp;&boxvr;&nbsp;classifiers                         | 存放分类模型的网络权值、预测输出的目录                      |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;model_KFR{i}.pkl        | 第`i`折模型的预测输出，数据结构：`list`                     |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;model_KFR{i}.pt         | 第`i`折模型的网络权值，使用`torch.load()`方法加载           |
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp;get_pred_raw.py         | 模型预测输出清洗程序，将输出存为`.pkl`文件                  |
| &ensp;&ensp;&boxvr;&nbsp;data                                | 存放数据集图片的目录                                        |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;dtd/images/baseline     | 存放原始数据集                                              |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;dtd/images/basic        | 存放基本变换扩充数据集                                      |
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp;dtd/images/gan          | 存放深度学习扩充数据集                                      |
| &ensp;&ensp;&boxvr;&nbsp;labels                              | 存放数据集标签的目录                                        |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;{diff}/4Fold_P{i}_test.csv | `diff`复合比例下，第`i`折模型的测试集划分                   |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;{diff}/4Fold_P{i}_train.csv | `diff`复合比例下，第`i`折模型的训练集划分                   |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;dict_KFold.py           | 本地划K折划分程序，将划分输出存为`.csv`文件                 |
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp;label_{method}.txt      | 使用`method`方法创建的数据记录\*，数据结构：`Path |Label`。 |
| &ensp;&ensp;&boxvr;&nbsp;scripts                             | 存放Python脚本的目录                                        |
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp;dataset_pruning.py      | 数据集修剪程序，将data中深度学习扩充的baseline部分删除      |
| &ensp;&ensp;&boxvr;&nbsp;ResNet.ipynb                        | 使用Notebook存储的模型训练、测试程序                        |
| &ensp;&ensp;&boxvr;&nbsp;README.md                           | 本程序文档                                                  |
| &ensp;&ensp;&boxvr;&nbsp;general_means.pt                    | 本组数据集的样本均值                                        |
| &ensp;&ensp;&boxvr;&nbsp;general_stds.pt                     | 本组数据集的样本方差                                        |
| &ensp;&ensp;&boxur;&nbsp;dict_parser.py                      | 数据集标签建立程序，生成的标签放入labels文件夹中            |

\*例：origin=对照组，basic=基本变换，gan=深度学习，以此类推。

* * *
#### 存放地址：

[GitHub](https://github.com/Voychek1024/Graduation_Project)

[OneDrive](https://1drv.ms/u/s!Ak7i9eRLkHfRg499frRiI75vpPOeJw?e=UGpf9j)

[百度云](https://pan.baidu.com/s/1vHsv6fgeg1ddkgrEmm2wZg?pwd=quwc)

其中，GitHub仅存储代码，以及小型文件；数据集与模型参数请从OneDrive或百度云下载。