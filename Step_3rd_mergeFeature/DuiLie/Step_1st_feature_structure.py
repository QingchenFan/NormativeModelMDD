import glob
import pandas as pd


# # --------DuiLie HC features --------
DLHClabel = pd.read_csv('/Volumes/QCI/NormativeModel/DuiLie/DLHClabel.csv')

DLHCGrayVol = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/DL/DLHC_GrayVol.csv')
DLHCGrayVol_df = pd.merge(DLHClabel, DLHCGrayVol, on='subID', how='inner')
DLHCGrayVol_df.to_csv('./DLHCGrayVol.csv', index=False)


DLHCSurfArea = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/DL/DLHC_SurfArea.csv')
DLHCSurfArea_df = pd.merge(DLHClabel, DLHCSurfArea, on='subID', how='inner')
DLHCSurfArea_df.to_csv('./DLHCSurfArea.csv', index=False)

DLHCThickAvg = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/DL/DLHC_ThickAvg.csv')
DLHCThickAvg_df = pd.merge(DLHClabel, DLHCThickAvg, on='subID', how='inner')
DLHCThickAvg_df.to_csv('./DLHCThickAvg.csv', index=False)

## -------- DuiLie MDD features --------
# Data135MDDlabel = pd.read_csv('/Volumes/QCI/NormativeModel/Data135/MDDlabel.csv')
# Data135MDDGrayVol = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/HCP_DATA135_Structure/Data135MDDGrayVol.csv')
# Data135MDDGrayVol_df = pd.merge(Data135MDDlabel, Data135MDDGrayVol, on='subID', how='inner')
# Data135MDDGrayVol_df.to_csv('./Data135MDDGrayVol.csv', index=False)
#
# Data135MDDSurfArea = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/HCP_DATA135_Structure/Data135MDDSurfArea.csv')
# Data135MDDSurfArea_df = pd.merge(Data135MDDlabel, Data135MDDSurfArea, on='subID', how='inner')
# Data135MDDSurfArea_df.to_csv('./Data135MDDSurfArea.csv', index=False)
#
# Data135MDDThickAvg = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/HCP_DATA135_Structure/Data135MDDThickAvg.csv')
# Data135MDDThickAvg_df = pd.merge(Data135MDDlabel, Data135MDDThickAvg, on='subID', how='inner')
# Data135MDDThickAvg_df.to_csv('./Data135MDDThickAvg.csv', index=False)
