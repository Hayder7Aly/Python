import os
import shutil
path=input('Enter a path where you cut:')
os.chdir(path)
ff=input('Enter a file or folder name :')
ff2=input('Enter a file name with path where you paste :')
shutil.move(ff,rf'{ff2}\{ff}')
input('completed!')
input()