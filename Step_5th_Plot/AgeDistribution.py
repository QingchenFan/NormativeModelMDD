import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# --------------------------------HC（健康组年龄分布）--------------------------------
# data = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/allHCfeature.csv')
# # 提取男性和女性的年龄数据
# male_age_data = data[data['sex'] == 1]['age']
# female_age_data = data[data['sex'] == 2]['age']
#
# # 设置绘图风格为Seaborn默认风格
# sns.set()
# sns.set_style('white')
# # 绘制直方图
# sns.histplot(data=data, x='age', hue='sex', multiple='stack')
# sns.despine()
# # 设置图表的标题和轴标签
# plt.title('Population by Age and Gender')
# plt.xlabel('Age')
# plt.ylabel('Population')
#
# # 添加图例
# plt.legend(['Male', 'Female'])
#
# # 显示图表
# plt.show()
# --------------------------MDD（疾病组年龄分布）---------------------------------
# 读取CSV文件
# data = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/andingMddGradientfeature_combat.csv')
#
# # 提取男性和女性的年龄数据
# male_age_data = data[data['sex'] == 1]['age']
# female_age_data = data[data['sex'] == 2]['age']
#
# # 设置绘图风格为Seaborn默认风格
# sns.set()
# sns.set_style('white')
# # 绘制直方图
# sns.histplot(data=data, x='age', hue='sex', multiple='stack')
# sns.despine()
# # 设置图表的标题和轴标签
# plt.title('Population by Age and Gender')
# plt.xlabel('Age')
# plt.ylabel('Population')
#
# # 添加图例
# plt.legend(['Male', 'Female'])
#
# # 显示图表
# plt.show()

# -----------------训练集-测试集数据分布-------------
#   # 1 - 第一阶段
# tr = pd.read_csv('./allHC_tr.csv')
# #tr = tr['age']
#
#
# te = pd.read_csv('./allHC_te.csv')
#
# # 使用Seaborn的distplot函数绘制直方图
# sns.distplot(tr['age'], bins=10, hist=True, kde=False, label='Train Data')
# sns.distplot(te['age'], bins=10, hist=True, kde=False, label='Test Data')
#
# # 添加图例
# plt.legend()
# # 显示图表
# plt.show()
    # 2  - 第二阶段（微调阶段数据集划分）
# tr_anding = pd.read_csv('./allHC_anding_tr.csv')
# #tr = tr['age']
#
#
# te_anding = pd.read_csv('./allHC_anding_te.csv')
#
# # 使用Seaborn的distplot函数绘制直方图
# sns.distplot(tr_anding['age'], bins=10, hist=True, kde=False, label='Train Data')
# sns.distplot(te_anding['age'], bins=10, hist=True, kde=False, label='Test Data')
#
# # 添加图例
# plt.legend()
# # 显示图表
# plt.show()

#    -----------------重叠放置HC MDD------------------------
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 读取两个CSV文件
# df1 = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/allHCGradientfeature.csv', usecols=['age'])
# df2 = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/andingMddGradientfeature_combat.csv', usecols=['age'])
#
# # 为数据框中的年龄列设置相同的名称
# df1.rename(columns={'age': 'age'}, inplace=True)
# df2.rename(columns={'age': 'age'}, inplace=True)
#
# # 使用Seaborn的distplot函数绘制直方图
# sns.distplot(df1['age'], hist=True, color='gray', kde=False, bins=40, label='HC')
# sns.distplot(df2['age'], hist=True, color='r',kde=False, bins=40, label='MDD')
# sns.despine()
# # 设置图表的标题和轴标签
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Population')
#
# # 添加图例
# plt.legend()
#
# # 显示图表
# plt.show()

