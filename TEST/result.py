import pandas as pd



RMSE = pd.read_pickle('./Data/Result/RMSE_estimate.pkl')
print('--RMSE--\n',RMSE)
res = pd.read_pickle('./Data/Result/RMSE_transfer.pkl')
print('--transfer-RMSE--\n',res)
rperson = pd.read_pickle('./Data/Result/Rho_transfer.pkl')
print('-Rho_transfer-\n',rperson)
pvalue = pd.read_pickle('./Data/Result/pRho_transfer.pkl')
print('-pRho_transfer-\n',pvalue)
smse = pd.read_pickle('./Data/Result/SMSE_transfer.pkl')
print('-SMSE_transfer-\n',smse)