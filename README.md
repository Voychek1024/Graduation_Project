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

#### 应用场景：材料图像
- 获取：DTD数据集
- 适用模型：ResNet34
- 指标：Top-1 Accuracy

#### 进展：
任务状态![status](https://img.shields.io/badge/status-working-orange)

- [x] 环境配置
- [x] CIFAR10：ResNet分类器
- [x] CIFAR10：GAN效果测试
- [ ] CIFAR10：训练整合
- [x] DTD：ResNet分类器
- [ ] DTD：GAN效果测试
- [ ] DTD：训练整合
- [ ] 结果分析
- [ ] 书写论文

#### 环境配置：
Anaconda3 (Python 3.8.x)

pytorch, numpy, opencv, matplotlib, joblib, sklearn