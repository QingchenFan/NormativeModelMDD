import numpy as np
import os
import pandas as pd
import pcntoolkit as ptk
import pickle
import matplotlib.pyplot as plt

# confidence interval calculation at x_forward
def confidence_interval(s2,x,z):
  CI=np.zeros((len(x_forward),4))
  for i,xdot in enumerate(x_forward):
    ci_inx=np.isin(x,xdot)
    S2=s2[ci_inx]
    S_hat=np.mean(S2,axis=0)
    n=S2.shape[0]
    CI[i,:]=z*np.power(S_hat/n,.5)
  return CI



# a simple function to quickly load pickle files
def ldpkl(filename: str):
    with open(filename, 'rb') as f:
        return pickle.load(f)


idps = ['LH_Vis_1','LH_Default_PFC_12','LH_DorsAttn_PrCv_1','LH_Default_pCunPCC_5','LH_SalVentAttn_TempOcc_1',
        'LH_Limbic_OFC_1','LH_Limbic_TempPole_5','LH_Cont_Par_3','LH_Cont_pCun_2','LH_Default_Temp_6',
        'RH_Vis_8','RH_Vis_18','RH_SomMot_3','RH_SomMot_15','RH_SomMot_30','RH_DorsAttn_Post_2',
        'RH_DorsAttn_Post_12','RH_SalVentAttn_Med_5','RH_Limbic_OFC_3','RH_Cont_Par_1'
        ]
pro_dir = '/Users/qingchen/Documents/code/NormativeModelMDD/Step_5th_Plot/Data/Result/'
if not os.path.isdir(pro_dir):
    os.mkdir(pro_dir)
os.chdir(pro_dir)
pro_dir = os.getcwd()



# -- 构建 MDD x y
HC_test = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/HCtest_I.csv')
print(HC_test)
#HC_test = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/andingMddGradientfeature.csv')
HC_test_X_test = (HC_test['age'] / 100).to_numpy(dtype=float)
print(HC_test_X_test.shape)
HC_test_Y_test = HC_test[idps].to_numpy(dtype=float)
print(HC_test_Y_test.shape)
anding_mdd_batch_effects_test = HC_test['sitenum'].to_numpy(dtype=int)
print(anding_mdd_batch_effects_test.shape)

with open('HC_test_X_test.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(HC_test_X_test), file)
with open('HC_test_Y_test.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(HC_test_Y_test), file)
with open('HC_test_tsbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(anding_mdd_batch_effects_test), file)

testcov = os.path.join(pro_dir, 'HC_test_X_test.pkl')  # training batch effects file (eg scanner_id, gender)  (columns: the various batch effects, rows: observations or subjects)
testresp = os.path.join(pro_dir, 'HC_test_Y_test.pkl')
tsbefile = os.path.join(pro_dir, 'HC_test_tsbefile.pkl')

log_dir = os.path.join(pro_dir, 'log_transfer/')
output_path = os.path.join(pro_dir, 'Transfer_Test/')
model_path = os.path.join('/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data/Result/Transfer/')  # path to the previously trained models
#model_path = os.path.join(pro_dir,'Transfer/')  # path to the previously trained models

outputsuffix = '_HC_test'
# --最终训练模型
yhat, s2, z_scores = ptk.normative.predict(covfile=testcov,
                                           respfile=None,
                                           tsbefile=tsbefile,
                                           inscaler='standardize',
                                           outscaler='standardize',
                                           linear_mu='True',
                                           random_intercept_mu='True',
                                           centered_intercept_mu='True',
                                           model_path=model_path,
                                           alg='hbr',
                                           log_path=log_dir,
                                           binary=True,
                                           output_path=output_path,
                                           outputsuffix=outputsuffix,
                                           inputsuffix='transfer',
                                           savemodel=True)



exit()
feature_names=['LH_Vis_1']


yhat_forward = pd.read_pickle('/Users/qingchen/Documents/code/NormativeModelMDD/Step_5th_Plot/Data/Result/yhat_estimate.pkl')
yhat_forward = yhat_forward.iloc[:,:].to_numpy(dtype=float)
print(yhat_forward)
x_forward=[20, 25, 30, 35, 40, 45, 50]

allHC_te = pd.read_csv('/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data/allHC_te.csv')
x=allHC_te[['age']]

# actual data
y = allHC_te[feature_names[0]]

# confidence Interval yhat+ z *(std/n^.5)-->.95 % CI:z=1.96, 99% CI:z=2.58
s2= pd.read_pickle('/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data/Result/ys2_estimate.pkl')
print(s2.shape)

CI_95=confidence_interval(s2,x,1.96)
CI_99=confidence_interval(s2,x,2.58)

# Creat a trejactroy for each point

fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot(x_forward,yhat_forward, linewidth=4, label='Normative trejactory')


ax.plot(x_forward,CI_95+yhat_forward, linewidth=2,linestyle='--',c='g', label='95% confidence interval')
ax.plot(x_forward,-CI_95+yhat_forward, linewidth=2,linestyle='--',c='g')

ax.plot(x_forward,CI_99+yhat_forward, linewidth=1,linestyle='--',c='k', label='99% confidence interval')
ax.plot(x_forward,-CI_99+yhat_forward, linewidth=1,linestyle='--',c='k')

ax.scatter(x,y,c='r')
plt.legend(loc='upper left')
plt.title('Normative trejectory')
plt.show()
plt.close()