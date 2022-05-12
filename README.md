# Graduation Project
2022 Shanghai University Graduation Project

#### 选题：

数据增强方法对材料图像处理增益的研究

**所需知识：python，图像处理，基础机器学习及深度学习**

#### 课题简介：
	数据增强方法在深度学习与机器学习中是解决小样本问题的常用方案之一。现有的数据增强方法种类较多，但其中并非所有的数据增强方法都适合材料图像的处理。针对现有的几种材料图像数据，筛选或组合现有的数据增强方法对其效果进行研究和探索，并尝试应用在常见的材料图像处理任务，在分类准确度或分割平均交并比等技术指标上取得有效的提升。通过本课题的研究，找到对于材料图像数据应用良好的数据增强方式，为进一步解决材料图像中的小样本难题提供可行的方案。

#### 思路大纲：
- 小样本数据集、分类问题
- 评价指标：Accuracy

#### 数据增强方法：
1. 基于基本图像处理技术
2. 基于深度学习（GAN）
3. 上述两者结合

#### 应用场景：材料图像
- 获取：DTD数据集（4折交叉实验）
- 适用模型：AlexNet、VGG、ResNet、ResNeXt、Inception、DenseNet、SENet
- 指标：Top-1 Accuracy（测试集、文献），训练时间
- 作图：Epoch-Error、Epoch-Loss图像（保留绘图原始数据）

#### 进展：
任务状态 ![status](https://img.shields.io/badge/status-working-orange)

选用数据集：
- [x] cifar10数据集（样例）
- [x] dtd数据集（对照组）
- [x] dtd数据集（基本增强扩充）
- [ ] dtd数据集（GAN增强扩充）
- [ ] dtd数据集（基本+GAN增强扩充）

选用神经网络：
- [x] ShuffleNet
- [x] VGG
- [x] ResNet
- [x] ResNeXt
- [x] MobileNet
- [x] DenseNet
- [x] SENet

#### 环境配置：
Anaconda3 (Python 3.8.x)

pytorch, numpy, opencv, matplotlib, joblib, sklearn