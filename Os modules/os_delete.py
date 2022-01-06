import os
import shutil
path=input('Enter a path in which you deleter a foder \ file : ')
os.chdir(path)
ff=input('Enter a file or folder name :')
if not os.path.exists(ff):
    print(f'such a file not in directory: {ff}')
else:
    shutil.rmtree(ff)