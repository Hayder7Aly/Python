import os 
path=input('Enter a path of folder in which you create folder :')
os.chdir(path)
folder=input('Enter a folder name :')
if os.path.exists(folder):
    print('Already exits :')
else:
    os.mkdir(folder)
input()