import pandas as pd
markname = 'Result_0508_5'
print('============== r-p estimate==================')
Rho_estimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/'+ markname +'/Rho_estimate.pkl')
pRho_estimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/'+ markname +'/pRho_estimate.pkl')

df_estimate = pd.concat([Rho_estimate, pRho_estimate], axis=1)  # 将两列拼接在一起，axis=1 表示按列拼接
df_estimate.columns = ['rvalue', 'pvalue']
print(df_estimate)


print('===============r-p transfer=================')

Rho_transfer = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/'+ markname +'/Rho_transfer.pkl')
pRho_transfer = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/'+ markname +'/pRho_transfer.pkl')

df_transfer = pd.concat([Rho_transfer, pRho_transfer], axis=1)  # 将两列拼接在一起，axis=1 表示按列拼接
df_transfer.columns = ['rvalue', 'pvalue']
print(df_transfer)


print('============= RMSE ===================')

RMSE_estimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/'+ markname +'/RMSE_estimate.pkl')
RMSE_transfer = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/'+ markname +'/RMSE_transfer.pkl')

df_RMSE = pd.concat([RMSE_estimate, RMSE_transfer], axis=1)  # 将两列拼接在一起，axis=1 表示按列拼接
df_RMSE.columns = ['RMSE_estimate', 'RMSE_transfer']
print(df_RMSE)

#print('============= Z-value ===================')
# Z_estimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/'+ markname +'/Z_estimate.pkl')
# Z_transfer = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/'+ markname +'/Z_transfer.pkl')
# print(Z_estimate)
# print(Z_transfer)


