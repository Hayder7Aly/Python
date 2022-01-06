import os 
import shutil
path=input('Enter a path in which you copy :')
os.chdir(path)
ff=input('Enter a file or folder name:')
ff2=input('Enter a path with folder where you paste :')
shutil.copytree(ff,rf'{ff2}\{ff}')
input()