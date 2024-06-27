import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# confidence interval calculation at x_forward

allHC = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/allstruc/combat/allHC_GrayVol_combat.csv')
brainRegion = allHC.columns.tolist()
del brainRegion[0:5]
allHC_X_train = (allHC[['sex','age']]).to_numpy(dtype=float)
allHC_Y_train = allHC[brainRegion].to_numpy(dtype=float)

def confidence_interval(s2,x,z):
  CI = np.zeros((len(x_forward),len(brainRegion)))
  for i,xdot in enumerate(x_forward):
    ci_inx = np.isin(x,xdot)
    S2 = s2[ci_inx]
    S_hat = np.mean(S2,axis=0)
    n = S2.shape[0]
    CI[i,:] = z*np.power(S_hat/n,.5)
  return CI
yhat_forward = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/yhat_allHCtest.pkl')   # 测试集的yhat
yhat_forward = yhat_forward.iloc[:,:].to_numpy(dtype=float)

x_forward=[20, 22, 24, 26, 28, 30, 32, 34, 36, 37]

x = allHC_X_train[:,1]    # 训练集的x 只取了年龄这一列
y = allHC_Y_train         # 训练集的y

s2 = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/ys2_AllHCestimate.pkl')   # 只有allHC训练集时，所输出的yhat
s2 = s2.iloc[:,:].to_numpy(dtype=float)

CI_95=confidence_interval(s2,x,1.96)
CI_99=confidence_interval(s2,x,2.58)

for idp_num,idp_name in enumerate(brainRegion):
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(x_forward,yhat_forward[:,idp_num], linewidth=4, label='Normative trejactory')


    ax.plot(x_forward,CI_95[:,idp_num]+yhat_forward[:,idp_num], linewidth=2,linestyle='--',c='g', label='95% confidence interval')
    ax.plot(x_forward,-CI_95[:,idp_num]+yhat_forward[:,idp_num], linewidth=2,linestyle='--',c='g')

    ax.plot(x_forward,CI_99[:,idp_num]+yhat_forward[:,idp_num], linewidth=1,linestyle='--',c='k', label='99% confidence interval')
    ax.plot(x_forward,-CI_99[:,idp_num]+yhat_forward[:,idp_num], linewidth=1,linestyle='--',c='k')

    ax.scatter(x,y[:,idp_num],c='r', label=idp_name)
    plt.legend(loc='upper right')
    plt.title('Normative trejectory')
    plt.savefig('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/png/'+idp_name+'.png')
    # plt.show()
    # plt.close()