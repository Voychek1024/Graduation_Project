#### StyleGAN_Playground
StyleGAN实现基于以下Repo：[stylegan2-ada-pytorch](https://github.com/NVlabs/stylegan2-ada-pytorch) ，可检阅该仓库的README.md以获取更多支持。

#### Low-Shot 训练、生成方法

数据集应以`.zip`形式进行存储。

使用如下代码训练：

```bash
python train.py --outdir=training-runs --data=%DATA%/%DATASET%.zip --gpus=1 --metrics=none
```

使用如下代码追加训练：

```bash
python train.py --outdir=training-runs --data=%DATA%/%DATASET%.zip --resume=%TRAINING-RUNS%/%DATASET%/%MODEL%.pkl --gpus=1 --metrics=none
```

使用如下代码生成：

```bash
python generate.py --outdir=%OUTPUT%/%DATASET% --network=%MODELS%/%DATASET%/%MODEL%.pkl --seeds=1-1000
```

其中，变量含义如下表所示：

| 变量名          | 变量含义                                    |
| --------------- | ------------------------------------------- |
| %DATA%          | 存放数据集的文件夹                          |
| %DATASET%       | 数据集名称，共47类                          |
| %TRAINING-RUNS% | training-runs文件夹，用于存放模型的快照输出 |
| %MODEL%         | 模型名称，例如network-snapshot-000160.pkl   |
| %OUTPUT%        | 存放输出图片的文件夹                        |

需要根据具体系统环境加以修改。

#### 免责声明

此PyTorch代码库并非对原始论文的完全复现，详细结果复现请参考[TensorFlow repo](https://github.com/mit-han-lab/data-efficient-gans/tree/master/DiffAugment-stylegan2)。

* * *

#### 存放地址：

[GitHub](https://github.com/Voychek1024/Graduation_Project)

[OneDrive](https://1drv.ms/u/s!Ak7i9eRLkHfRg499frRiI75vpPOeJw?e=UGpf9j)

[百度云](https://pan.baidu.com/s/1vHsv6fgeg1ddkgrEmm2wZg?pwd=quwc)

其中，GitHub仅存储代码，以及小型文件；数据集与模型参数请从OneDrive或百度云下载。
