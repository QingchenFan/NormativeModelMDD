import nibabel as nib
import glob

from scipy.io import savemat

FCpath = '/Volumes/qingchen/HCPData/HCPSchaefer400FC/*'

file = glob.glob(FCpath)

for i in file:
    subId = i[-10:]
    Fcpath = glob.glob(i+'/*-LR*')
    if len(Fcpath) == 0:
        print('》》》》',i)
        continue
    FCData = nib.load(Fcpath[0]).get_fdata()
    savemat('/Volumes/qingchen/HCPData/HCPmat/' + subId + '_Schaefer400FC.mat', {'data':FCData})