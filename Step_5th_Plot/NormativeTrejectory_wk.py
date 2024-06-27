import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# confidence interval calculation at x_forward
def confidence_interval(s2, x, z):
    CI = np.zeros((len(x), 400))
    for i, xdot in enumerate(x):

        ci_inx = np.isin(x, xdot)
        print('--',x)

        S2 = s2[ci_inx]
        S_hat = np.mean(S2, axis=0)
        n = S2.shape[0]
        CI[i, :] = z * np.power(S_hat / n, .5)
    return CI


    # forward model data
forward_yhat = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/yhat_allHCtest.pkl')
yhat_forward=forward_yhat

x_forward = np.array([20, 22, 24, 26, 28, 30, 32, 34, 36, 37])

covariate_normsample = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/allstruc/combat/allHC_GrayVol_combat.csv',index_col=0)
brainRegion = covariate_normsample.columns.tolist()
del brainRegion[0:5]
x = covariate_normsample['age'].values

# actual data
y = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/allstruc/combat/allHC_GrayVol_combat.csv')
y = y.values[:,5:]

    # confidence Interval yhat+ z *(std/n^.5)-->.95 % CI:z=1.96, 99% CI:z=2.58
s2 = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/ys2_allHCtest.pkl')
print(s2)

CI_95 = np.array(confidence_interval(s2, x_forward, 1.96))
print('CI_95',CI_95)

CI_99 = np.array(confidence_interval(s2, x_forward, 2.58))
print('CI_99',CI_99[:,0])
# yhat就是预测值
# Creat a trejactroy for each point

for idp_num, idp_name in enumerate(brainRegion):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x_forward, np.array(yhat_forward)[:, idp_num], linewidth=4, label='Normative trejactory')

        ax.plot(x_forward, CI_95[:, idp_num] + np.array(yhat_forward)[:, idp_num], linewidth=2, linestyle='--', c='g',
                label='95% confidence interval')
        ax.plot(x_forward, -CI_95[:, idp_num] + np.array(yhat_forward)[:, idp_num], linewidth=2, linestyle='--', c='g')

        ax.plot(x_forward, CI_99[:, idp_num] + np.array(yhat_forward)[:, idp_num], linewidth=1, linestyle='--', c='k',
                label='99% confidence interval')
        ax.plot(x_forward, -CI_99[:, idp_num] + np.array(yhat_forward)[:, idp_num], linewidth=1, linestyle='--', c='k')

        ax.scatter(x, y[:, idp_num], c='r', label=idp_name)
        plt.legend(loc='upper left')
       # plt.title('Normative trejectory of' + name + ' in ' + sex + ' cohort')
        plt.savefig('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/png/' + idp_name + '.png',dpi=300)
        # plt.show()
        # plt.close()

