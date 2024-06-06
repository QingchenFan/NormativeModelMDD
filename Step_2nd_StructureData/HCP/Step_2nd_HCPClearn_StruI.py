import glob
import pandas as pd
datapath = glob.glob('/Volumes/QCI/HCP_Struc/hcp_res/*')
tmp = []

for i in datapath:
    sn = ['GrayVol', 'ThickAvg', 'SurfArea']
    for j in sn:
        print(i)
        subID = i.split('/')[-1]

        rhp = i + '/' + subID+'_rh.txt'

        rh_data = pd.read_csv(rhp,skiprows = 61, delimiter = '\t',header=None)
        rh_data.columns = ['Column1']
        rh_data = rh_data['Column1'].str.split(n=9, expand=True)
        rh_data.columns = ['StructName', 'NumVert', 'SurfArea' ,'GrayVol', 'ThickAvg', 'ThickStd', 'MeanCurv', 'GausCurv', 'FoldInd', 'CurvInd']
        rh = rh_data[['StructName',j]].T

        lhp = i + '/' + subID + '_lh.txt'
        lh_data = pd.read_csv(lhp,skiprows = 61, delimiter = '\t',header=None)
        lh_data.columns = ['Column1']
        lh_data = lh_data['Column1'].str.split(n=9, expand=True)
        lh_data.columns = ['StructName', 'NumVert', 'SurfArea' ,'GrayVol', 'ThickAvg', 'ThickStd', 'MeanCurv', 'GausCurv', 'FoldInd', 'CurvInd']
        lh = lh_data[['StructName', j]].T

        res = pd.concat([rh,lh],axis=1, ignore_index=True)
        #print(res)
        res.insert(0, 'subId', [' ', subID])
        print(res)
        res.to_csv(i +'/'+subID+'_'+j+'.csv',index=False)



