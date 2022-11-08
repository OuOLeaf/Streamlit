import os
import glob
import shutil

hPath = r'D:\Dropbox\Andy\streamlit\finanical_standard'
gPath = r'C:\Users\user\Documents\GitHub\finan_std'
dfPath = glob.glob(gPath + "/*.py")

for i in dfPath:
    os.remove(i)  
mfPath = glob.glob(hPath + "/*.py")
for j in mfPath:
    file = '\\' + j.split('\\')[-1]
    # print(file)
    shutil.copy(hPath + file, gPath + file)

