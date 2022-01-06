import os 
path=input('Enter a path of folder in which you create file :')
os.chdir(path)
file=input('Enter file name:')
if os.path.exists(file):
    print('Already exits :')
else:
    open(file,'a').close()
input()