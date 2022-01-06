import os
import shutil
path=input('Enter a path where you check the data :')
os.chdir(path)
fileiter=os.walk(path)
for current_directory,folders_name,files_name in fileiter:
    print(f'current_directory:{current_directory}')
    print(f'folders_name:{folders_name}')
    print(f'file_names:{files_name}')