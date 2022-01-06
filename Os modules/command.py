import os
import shutil
print('\t\t\tCOMMAND IN PYTHON !')
print('\t\t----------------------------')
print('\t\t|Enter for create folder : 1|')
print('\t\t|Enter for create file   : 2|')
print('\t\t|Enter for delete folder : 3|')
print('\t\t|Enter for copy   folder : 4|')
print('\t\t|Enter for move   folder : 5|')
print('\t\t|Enter for check  data   : 6|')
print('\t\t|Enter for close programe: 7|')
print('\t\t-----------------------------')
while True:
    choice=input('Enter a number for following :')
    if choice=='1':
        path=input('Enter a path where you create folder :')
        if not os.path.exists(path):
            print('Please enter correct path :')
            continue
        else:
            os.chdir(path)
        folder=input('Enter a folder name :')
        if os.path.exists(folder):
            print(f'This folder already exits {folder}')
        else:
            os.mkdir(folder)
    elif choice=='2':
        path=input('Enter a path where you create file:')
        if not os.path.exists(path):
            print('Please enter correct path:')
            continue
        else:
            os.chdir(path)
        file=input('Enter a file name :')
        if os.path.exists(file):
            print('This file is already exits :')
        else:
            open(file,'a').close()
    elif choice=='3':
        path=input('Enter a path where you delete folder or file :')
        if not os.path.exists(path):
            print('Please Enter correct path')
            continue
        else:
            os.chdir(path)
        delete=input('Enter a folder or file you want delete :')
        if not os.path.exists(delete):
            print('Such a folder not in directory :')
        else:
            shutil.rmtree(delete)
    elif choice=='4':
        path=input('Enter a path where you copy :')
        if not os.path.exists(path):
            print('Please Enter correct path')
            continue
        else:
            os.chdir(path)
        copy=input('Enter a folder or file name you want copy :')
        if not os.path.exists(copy):
            print('Such folder  not in directory:')
            continue
        else:
            paste=input('Enter a path where you paste :')
            if not os.path.exists(paste):
                print('Please enter correct path :')
            else:
                os.chdir(path2)
                shutil.copytree(copy,rf'{paste}\{copy}')
    elif choice=='5':
        path=input('Enter a path where you move or cut :')
        if not os.path.exists(path):
            print('Please enter correct path :')
        else:
            os.chdir(path)
        ff=input('Enter a folder or file name :')
        if not os.path.exits(ff):
            print('Such a folder nor in directory :')
        else:
        