import pandas as pd
import numpy as np

yhat_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/yhat_AllHCestimate.pkl')

label= pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/GradientFeature/allGrad/combat/allHC_Gradientfeature_combat.csv')

brainRegion = label.columns.tolist()
del brainRegion[0:5]
m = []
for num,re in enumerate(brainRegion):
    a = yhat_AllHCestimate[num]
    b = label[re]
    MAE = np.mean(np.abs(a - b))
    m.append(MAE)
mae = pd.DataFrame(m)

Rho_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/Rho_AllHCestimate.pkl')
pRho_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/pRho_AllHCestimate.pkl')
RMSE_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/RMSE_AllHCestimate.pkl')
SMSE_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_OnlyHC_kk/fqc/SMSE_AllHCestimate.pkl')


df_sum = pd.concat([Rho_AllHCestimate, pRho_AllHCestimate, RMSE_AllHCestimate,SMSE_AllHCestimate,mae], axis=1)  # 将两列拼接在一起，axis=1 表示按列拼接
df_sum.columns = ['Rho_estimate','pRho_estimate','RMSE_estimate', 'SMSE_estimate','MAE']

df_sum.to_csv('./GrayVol_ResSum.csv')

