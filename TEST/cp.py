import glob
from shutil import copy, copytree

path = '/n07dat01/OpenData/HCP1200/*/T1w/'
path = '/Volumes/QCI/HCP/testHCP/HCP1200/*/T1w/'
datapath = glob.glob(path)

for i in datapath:
    print(i)
    subId = i.split('/')[-3]
    sp = i + subId
    tp = '/Volumes/QCI/HCP/tar/'
    copytree(sp,tp + subId)
