#### 深度学习方法组
任务概述：GAN生成对抗网络

- [x] 细分：StyleGAN
- [x] 现实意义
- [x] 训练方法（详见[StyleGAN_playground](https://github.com/Voychek1024/Graduation_Project/tree/main/stylegan_playground)）
- [x] 生成方法（保存标签）

在深度学习方法增强后的数据集上，使用ResNet50模型，训练、测试，以及收集结果
* * *
##### StyleGAN模型选择：
| 序号 | 数据大类 | 训练周期(kimg)\* |
| ---- | -------- | -------------- |
|0001|banded|88|
|0002|blotchy|200+60|
|0003|braided|200+40|
|0004|bubbly|200+100|
|0005|bumpy|200+100|
|0006|chequered|140|
|0007|cobwebbed|200+100|
|0008|cracked|200|
|0009|crosshatched|200+100 **(反向筛选)**|
|0010|crystalline|200+100|
|0011|dotted|200+100|
|0012|fibrous|200|
|0013|flecked|200|
|0014|freckled|200|
|0015|frilly|200+100|
|0016|gauzy|200+100|
|0017|grid|200|
|0018|grooved|200+100|
|0019|honeycombed|200+100|
|0020|interlaced|200+100|
|0021|knitted|200+100|
|0022|lacelike|200+60|
|0023|lined|200|
|0024|marbled|200+100|
|0025|matted|200|
|0026|meshed|200+20|
|0027|paisley|160|
|0028|perforated|200+80|
|0029|pitted|200+60|
|0030|pleated|200|
|0031|polka|dotted|
|0032|porous|160|
|0033|potholed|200|
|0034|scaly|180|
|0035|smeared|180|
|0036|spiralled|160|
|0037|sprinkled|120|
|0038|stained|200|
|0039|stratified|200|
|0040|striped|200+100|
|0041|studded|200+100|
|0042|swirly|200+60|
|0043|veined|160|
|0044|waffled|200+80|
|0045|woven|160|
|0046|wrinkled|180|
|0047|zigzagged|140|

\*含"+"符号即对模型使用了resume方法追加训练

#### 目录结构：

| 相对路径                                                     | 描述                                                         |
| ------------------------------------------------------------ | :----------------------------------------------------------- |
| &ensp;&ensp;&boxvr;&nbsp;classifiers                         | 存放分类模型的网络权值、预测输出的目录                       |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;model_KFR{i}.pkl        | 第`i`折模型的预测输出，数据结构：`list`                      |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;model_KFR{i}.pt         | 第`i`折模型的网络权值，使用`torch.load()`方法加载            |
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp;get_pred_raw.py         | 模型预测输出清洗程序，将输出存为`.pkl`文件                   |
| &ensp;&ensp;&boxvr;&nbsp;data                                | 存放数据集图片的目录                                         |
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp;dtd/images/{category}   | `category`类图片的目录，例如banded等                         |
| &ensp;&ensp;&boxvr;&nbsp;labels                              | 存放数据集标签的目录                                         |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;4Fold_P{i}_test.csv     | 第`i`折模型的测试集划分，数据结构：`Path | Label`            |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;4Fold_P{i}_train.csv    | 第`i`折模型的训练集划分，数据结构同上                        |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;dict_KFold.py           | 本地划K折划分程序，将划分输出存为`.csv`文件                  |
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp;label_{method}.txt      | 使用`method`方法创建的数据记录\*，数据结构：`Path |Label`。  |
| &ensp;&ensp;&boxvr;&nbsp;models                              | 存放StyleGAN生成器模型的目录                                 |
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp;{category}/snapshot.pkl | `category`类生成器模型权值，后缀数字代表训练周期             |
| &ensp;&ensp;&boxvr;&nbsp;output                              | 存放模型直接输出的目录                                       |
| &ensp;&ensp;&boxvr;&nbsp;output_analysis                     | 存放对模型直接输出分析绘图的目录                             |
| &ensp;&ensp;&ensp;&ensp;&boxvr; figs                         | 文件格式`{category}.stds.png`，含该类生成图片方差均值、最大/小值 |
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp;stds                    | 文件格式`{category}.stds`，含该类生成图片的方差数组          |
| &ensp;&ensp;&boxvr;&nbsp;pruned                              | 存放修剪删除图片的目录                                       |
| &ensp;&ensp;&boxvr;&nbsp;scripts                             | 存放Python脚本的目录                                         |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;dataset_pruning.py      | 数据集修剪程序，按给定方差阈值筛出图片至`pruned`中           |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;dir_management.py       | 目录维护程序，为`output`，以及`pruned`文件夹创建47个子类别   |
| &ensp;&ensp;&ensp;&ensp;&boxvr;&nbsp;output_analysis.py      | 输出分析程序，将结果存至`output_analysis/stds`中             |
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp;stds_analysis.py        | 方差绘图程序，将结果存至`output_analysis/figs`中             |
| &ensp;&ensp;&boxvr;&nbsp;StyleGAN                            | 存放StyleGAN生成器模型的目录                                 |
| &ensp;&ensp;&ensp;&ensp;&boxur;&nbsp;output_automation.py    | 自动化输出程序，为每个大类输出1000张图片                     |
| &ensp;&ensp;&boxvr;&nbsp;ResNet.ipynb                        | 使用Notebook存储的模型训练、测试程序                         |
| &ensp;&ensp;&boxvr;&nbsp;README.md                           | 本程序文档                                                   |
| &ensp;&ensp;&boxvr;&nbsp;general_means.pt                    | 本组数据集的样本均值                                         |
| &ensp;&ensp;&boxvr;&nbsp;general_stds.pt                     | 本组数据集的样本方差                                         |
| &ensp;&ensp;&boxur;&nbsp;dict_parser.py                      | 数据集标签建立程序，生成的标签放入labels文件夹中             |

\*例：origin=对照组，basic=基本变换，gan=深度学习，以此类推。

* * *
#### 存放地址：

[GitHub](https://github.com/Voychek1024/Graduation_Project)

[OneDrive](https://1drv.ms/u/s!Ak7i9eRLkHfRg499frRiI75vpPOeJw?e=UGpf9j)

[百度云](https://pan.baidu.com/s/1vHsv6fgeg1ddkgrEmm2wZg?pwd=quwc)

其中，GitHub仅存储代码，以及小型文件；数据集与模型参数请从OneDrive或百度云下载。