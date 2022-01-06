import os
path=input('Enter a path where you create folder inside folder :')
os.chdir(path)
folder=input('Enter a folder Name :')
folder2=input('Enter 2nd folder name :')
if os.path.exists(folder):
    print('Already exits :')
else:
    os.makedirs(rf'{folder}\{folder2}')