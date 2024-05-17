import pandas as pd

rperson = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result0428/Rho_estimate.pkl')
print('-Rho_transfer-\n',rperson)
pvalue = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result0428/pRho_estimate.pkl')
print('-pRho_transfer-\n',pvalue)

df = pd.concat([rperson, pvalue], axis=1)  # 将两列拼接在一起，axis=1 表示按列拼接
df.columns = ['rvalue', 'pvalue']
df.to_csv('./prvalue.csv')