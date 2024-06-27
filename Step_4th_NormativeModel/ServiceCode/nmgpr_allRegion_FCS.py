import os
import pandas as pd
import pcntoolkit as ptk
import pickle


# --构建模型的x、y
allHC = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/GradientFeature/allGrad/combat/allHC_Gradientfeature_combat.csv')
anding = allHC.loc[allHC['site'] == 'anding']                                               # 获取site = "anding"
                                                                      # 加一列，标识站点 - 0
allHCP = allHC.loc[allHC['site'] != 'anding']    # 获取其他站点的数据(此时的allHC,从allHC中排除了

#--要训练的脑区
brainRegion = allHC.columns.tolist()
del brainRegion[0:5]

idps = brainRegion

# --构建模型的x、y
pro_dir = '/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data_struc/Result_GPR_all/'
if not os.path.isdir(pro_dir):
    os.mkdir(pro_dir)
os.chdir(pro_dir)
pro_dir = os.getcwd()
allHC_X_train = (allHC[['sex','age']]).to_numpy(dtype=float)
allHC_Y_train = allHC[idps].to_numpy(dtype=float)



with open('allHC_X_train.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(allHC_X_train), file)

with open('allHC_Y_train.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(allHC_Y_train), file)


# --生成对应路径，方便传入参数
allHC_covfile = os.path.join(pro_dir,'allHC_X_train.pkl')  # covariates (eg age) the training samples (columns: covariates, rows: observations or subjects)
allHC_respfile = os.path.join(pro_dir,'allHC_Y_train.pkl')  # measurements  (eg cortical thickness) of the training samples (columns: the various features/ROIs, rows: observations or subjects)
output_path = os.path.join(pro_dir, 'Models/')  # output path, where the models will be written
log_dir = os.path.join(pro_dir, 'log/')
if not os.path.isdir(output_path):
    os.mkdir(output_path)
if not os.path.isdir(log_dir):
    os.mkdir(log_dir)

outputsuffix = '_AllHC_estimate'
# --训练模型
ptk.normative.estimate(covfile=allHC_covfile,
                       respfile=allHC_respfile,
                       cvfolds=10,
                       alg='gpr',
                       log_path=log_dir,
                       output_path=output_path,
                       outputsuffix=outputsuffix,
                       savemodel=True)

# 使用虚拟数据，构建轨迹线，首先是使用虚拟数据为测试集，得到yhat
allHCtest_covariate = {'sex': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                          'age': [20, 22, 24, 26, 28, 30, 32, 34, 36, 37]}
allHCtest_covariate = pd.DataFrame(data=allHCtest_covariate)
with open('allHCtest_covariate.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(allHCtest_covariate), file)
allHC_testcovfile = os.path.join(pro_dir, 'allHCtest_covariate.pkl')
outputsuffix = '_allHC_test'
# --训练模型
ptk.normative.estimate(covfile=allHC_covfile,
                       respfile=allHC_respfile,
                       testcov=allHC_testcovfile,
                       cvfolds=None,
                       alg='gpr',
                       log_path=log_dir,
                       output_path=output_path,
                       outputsuffix=outputsuffix,
                       savemodel=True)