import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
# ---------直方图--------------

#
# gray = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_FCS_10K_OnlyHC/FCS_ResSum.csv')
# y = gray['RMSE_estimate']       # TODO
#
# label= pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/FCSFeature/allFCS/combat/allHC_FCSfeature_combat.csv')
# brainRegion = label.columns.tolist()
# del brainRegion[0:5]
# x = brainRegion
# plt.figure(figsize=(20, 8))
# plt.bar(x, y)
# # 设置x轴和y轴的标签
# plt.xlabel('400-Region-FCS')  # TODO
# plt.ylabel('Values')
# # 旋转x轴标签45度
# #plt.xticks(rotation=45, ha='right', fontsize=10)
# # 隐藏x轴标签
# plt.xticks([])
# # 设置标题
# plt.title('RMSE - Values')       # TODO
#
# # 显示图像
# plt.show()


# ---------箱体图-散点 一组-------------
# Rho_estimate = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/wkk/region_r_p_values.csv')
# y = Rho_estimate['R_Value']
# fqc = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/GrayVol_ResSum.csv')
# y = fqc['Rho_estimate']
# plt.figure(figsize=(8, 6))
# jitter = np.random.normal(0, 0.05, len(y))  # 为散点添加抖动
# plt.scatter(np.ones_like(y) + jitter, y, color="red", alpha=0.7)
# box = plt.boxplot(y, patch_artist=True, boxprops=dict(facecolor="lightblue"))
#
# # 设置坐标轴刻度
# plt.xticks([1], ["Data"])
# plt.title("Box Plot and Scatter Plot of the Data")
# plt.xlabel("Data")
# plt.ylabel("Value")
# plt.grid(True)
# plt.show()

# # # ---------------------箱体图-散点-多组数据-------------------------------------------
# gray = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/GrayVol_ResSum.csv')
# gradient = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_Gradient_10K_OnlyHC/GRadient_ResSum.csv')
# fcs= pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_FCS_10K_OnlyHC/FCS_ResSum.csv')
# # y1 = gray['Rho_estimate']
# # y2 = gradient['Rho_estimate']
# # y3 = fcs['Rho_estimate']
# #
# # y1 = gray['RMSE_estimate']
# # y2 = gradient['RMSE_estimate']
# # y3 = fcs['RMSE_estimate']
#
# y1 = gray['MAE']
# y2 = gradient['MAE']
# y3 = fcs['MAE']
# plt.figure(figsize=(12, 12))
# bp = plt.boxplot([y1, y2, y3], patch_artist=True, labels=["Group 1", "Group 2", "Group 3"],
#                  showfliers=False, showbox=True, showcaps=True, showmeans=False)
#
# # 设置箱体图的颜色和线条样式
# for box in bp['boxes']:
#     box.set(color='#826E81', linewidth=1, alpha=0.7)
# for whisker in bp['whiskers']:
#     whisker.set(color='#826E81', linewidth=2)
# for cap in bp['caps']:
#     cap.set(color='#826E81', linewidth=2)
# for median in bp['medians']:
#     median.set(color='#79545F', linewidth=2.5)
#
# # 为每组添加随机抖动的散点
# for i, box in enumerate(bp['boxes']):
#     data = [y1, y2, y3][i]
#     jitter = np.random.normal(0, 0.12, len(data))
#     plt.scatter(np.ones_like(data) * (i+1) + jitter, data, color="#CDD2D2", alpha=0.7)
#
# # 去掉图表的顶部和右侧线条
# ax = plt.gca()
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
#
# # 加粗x轴和y轴的线条
# ax.spines['left'].set_linewidth(2)
# ax.spines['bottom'].set_linewidth(2)
#
# # 去除x轴和y轴上的小刻度线
# ax.tick_params(axis='both', length=0)
#
# # 设置坐标轴刻度和标题
# plt.xticks([1, 2, 3], ["GrayVol", "Gradient", "FCS"],size=16)
# plt.yticks(size=16)
# #plt.title("Box Plots and Scatter Plots of Three Groups")
# plt.xlabel("Feature",fontsize=16,labelpad=20)
# plt.ylabel("MAE",fontsize=16,labelpad=20)
# plt.grid(False)
# plt.show()

#

