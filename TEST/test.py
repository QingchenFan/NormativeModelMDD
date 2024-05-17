import os
import pandas as pd
import pcntoolkit as ptk
import numpy as np
import pickle
from matplotlib import pyplot as plt

allHC = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/allHCfeature.csv')
anding = allHC.loc[allHC['site'] == 'anding']                                   # 获取site = "anding"
anding['sitenum'] = 0                                                           # 加一列，标识站点 - 0

allHC = allHC.loc[allHC['site'] != 'anding']                                    # 获取其他站点的数据(此时的allHC,从allHC中排除了anding 站点
sites = allHC['site'].unique()                                                  # 获取其他站点名称

allHC['sitenum'] = 0

# age sex 分布
f, ax = plt.subplots(figsize=(12, 12))

for i,s in enumerate(sites):
    idx = allHC['site'] == s
    allHC['sitenum'].loc[idx] = i                                                # 为每一个站点进行标识 - 0 1 2 ...

    print('site',s, sum(idx))
    ax.scatter(allHC['age'].loc[idx], allHC['MeanGradient'].loc[idx])

ax.legend(sites)
ax.set_ylabel('MeanGradient')
ax.set_xlabel('age')
#-- train data \ test data
tr = np.random.uniform(size=allHC.shape[0]) > 0.2                                # 形成一个随机抽样(将AllHC的数据分为训练集和测试集
te = ~tr
allHC_tr = allHC.loc[tr]
allHC_te = allHC.loc[te]                                                         # 将AllHC中数据一分为2 ture false


tr = np.random.uniform(size=anding.shape[0]) > 0.2                               # 将anding 数据也形成一个随机抽样,形成训练集、测试集
te = ~tr

anding_tr = anding.loc[tr]                                                       # 训练集
anding_te = anding.loc[te]                                                       # 测试集

print('sample size check')
for i,s in enumerate(sites):
    idx = allHC_tr['site'] == s
    idxte = allHC_te['site'] == s
    print(i,s, sum(idx), sum(idxte))

#-- AllHC 分成训练集、测试集并保存到CSV文件中，anding同样操作
processing_dir = "/Users/qingchen/Documents/code/NormativeModelMDD/TEST/Data"
if not os.path.isdir(processing_dir):
    os.mkdir(processing_dir)
allHC_tr.to_csv(processing_dir + '/allHC_tr.csv')
allHC_te.to_csv(processing_dir + '/allHC_te.csv')
anding_tr.to_csv(processing_dir + '/allHC_anding_tr.csv')
anding_te.to_csv(processing_dir + '/allHC_anding_te.csv')

#--要训练的脑区
brainRegion = allHC.columns.tolist()
del brainRegion[0:4]
del brainRegion[-1:]

idps = brainRegion
# idps = ['LH_Vis_21','LH_Vis_22','LH_Vis_23','LH_Vis_24','LH_Vis_25','LH_Vis_26',
#         'LH_Vis_27','LH_Vis_28','LH_Vis_29','LH_Vis_30']
#--构建模型的x、y
idps = ['RH_Vis_26','RH_Vis_27','RH_Vis_28','RH_Vis_29','RH_Vis_30']
pro_dir = '/Users/qingchen/Documents/code/NormativeModelMDD/TEST/Data/Result'
if not os.path.isdir(pro_dir):
    os.mkdir(pro_dir)
os.chdir(pro_dir)
pro_dir = os.getcwd()

X_train = (allHC_tr['age']/100).to_numpy(dtype=float)
#print(X_train)
Y_train = allHC_tr[idps].to_numpy(dtype=float)
#print(Y_train)
batch_effects_train = allHC_tr[['sitenum']].to_numpy(dtype=int)

with open('X_train.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_train), file)
with open('Y_train.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_train), file)
with open('trbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_train), file)


X_test = (allHC_te['age']/100).to_numpy(dtype=float)
Y_test = allHC_te[idps].to_numpy(dtype=float)

batch_effects_test = allHC_te[['sitenum']].to_numpy(dtype=int)
with open('X_test.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_test), file)
with open('Y_test.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_test), file)
with open('tsbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_test), file)


# a simple function to quickly load pickle files
def ldpkl(filename: str):
    with open(filename, 'rb') as f:
        return pickle.load(f)
#--生成对应路径，方便传入参数
respfile = os.path.join(pro_dir, 'Y_train.pkl')       # measurements  (eg cortical thickness) of the training samples (columns: the various features/ROIs, rows: observations or subjects)
covfile = os.path.join(pro_dir, 'X_train.pkl')        # covariates (eg age) the training samples (columns: covariates, rows: observations or subjects)
testrespfile_path = os.path.join(pro_dir, 'Y_test.pkl')       # measurements  for the testing samples
testcovfile_path = os.path.join(pro_dir, 'X_test.pkl')        # covariate file for the testing samples

trbefile = os.path.join(pro_dir, 'trbefile.pkl')      # training batch effects file (eg scanner_id, gender)  (columns: the various batch effects, rows: observations or subjects)
tsbefile = os.path.join(pro_dir, 'tsbefile.pkl')      # testing batch effects file

output_path = os.path.join(pro_dir, 'Models/')    #  output path, where the models will be written

log_dir = os.path.join(pro_dir, 'log/')
if not os.path.isdir(output_path):
    os.mkdir(output_path)
if not os.path.isdir(log_dir):
    os.mkdir(log_dir)
outputsuffix = '_estimate'
#--训练模型
ptk.normative.estimate(covfile=covfile,
                       respfile=respfile,
                       tsbefile=tsbefile,
                       trbefile=trbefile,
                       cvfolds = 2,
                       #inscaler='standardize',
                       #outscaler='standardize',
                       #linear_mu='True',
                       #random_intercept_mu='True',
                       #centered_intercept_mu='True',
                       alg='hbr',
                       log_path=log_dir,
                       binary=True,
                       output_path=output_path,
                       testcov= testcovfile_path,
                       testresp = testrespfile_path,
                       outputsuffix=outputsuffix,
                       savemodel=True)
#----------------------------微调模型------------------------------------
# --构建模型的x、y
X_adapt = (anding_tr['age']/100).to_numpy(dtype=float)
Y_adapt = anding_tr[idps].to_numpy(dtype=float)
#batch_effects_adapt = icbm_tr[['sitenum','sex']].to_numpy(dtype=int)
batch_effects_adapt = anding_tr[['sitenum']].to_numpy(dtype=int)

with open('X_adaptation.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_adapt), file)
with open('Y_adaptation.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_adapt), file)
with open('adbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_adapt), file)

# Test data (new dataset)
X_test_txfr = (anding_te['age']/100).to_numpy(dtype=float)
Y_test_txfr = anding_te[idps].to_numpy(dtype=float)
#batch_effects_test_txfr = icbm_te[['sitenum','sex']].to_numpy(dtype=int)
batch_effects_test_txfr = anding_te[['sitenum']].to_numpy(dtype=int)

with open('X_test_txfr.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_test_txfr), file)
with open('Y_test_txfr.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_test_txfr), file)
with open('txbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_test_txfr), file)

respfile = os.path.join(pro_dir, 'Y_adaptation.pkl')
covfile = os.path.join(pro_dir, 'X_adaptation.pkl')
testrespfile_path = os.path.join(pro_dir, 'Y_test_txfr.pkl')
testcovfile_path = os.path.join(pro_dir, 'X_test_txfr.pkl')
trbefile = os.path.join(pro_dir, 'adbefile.pkl')
tsbefile = os.path.join(pro_dir, 'txbefile.pkl')

log_dir = os.path.join(pro_dir, 'log_transfer/')
output_path = os.path.join(pro_dir, 'Transfer/')
model_path = os.path.join(pro_dir, 'Models/')  # path to the previously trained models
print(model_path)
outputsuffix = '_transfer'
#--最终训练模型
yhat, s2, z_scores = ptk.normative.transfer(covfile=covfile,
                                            respfile=respfile,
                                            tsbefile=tsbefile,
                                            trbefile=trbefile,
                                            cvfolds = 2,
                                            #inscaler='standardize',
                                            #outscaler='standardize',
                                            #linear_mu='True',
                                            #random_intercept_mu='True',
                                            #centered_intercept_mu='True',
                                            model_path = model_path,
                                            alg='hbr',
                                            log_path=log_dir,
                                            binary=True,
                                            output_path=output_path,
                                            testcov= testcovfile_path,
                                            testresp = testrespfile_path,
                                            outputsuffix=outputsuffix,
                                            savemodel=True)
