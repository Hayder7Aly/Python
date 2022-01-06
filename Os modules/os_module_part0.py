# first we all import os module :
# getcwd() is used for check the path of folder in which we code or hardisk :
# mkdir we know about in git bash is used for creat foder:
# os.path.exits is used for check the folder is already exits or not except error:
# as we know already how can create file we use open for file creation and end of line we used close() the excutition of programme :
# we can create any where in computer memory folder and file with use of path in this programee i am use mkdir and write path and create a folder :
# we can use chdir its mean change directory is used for change folder or hardisk and create folders or files:
# listdir means list directory is used for check the all folder in hard drive :
# join is used for print path and folder or file name :

import os
# os.chdir('E:\ ')
# open('files.txt','a').close()
# os.mkdir('movies')
# os.mkdir('E:\ movies')
# print(os.getcwd())
# os.mkdir('haider')
# if os.path.exists('haider'):
#     print('Already exits :')
# else:
#     os.mkdir('haider')
# open('file.py','a').close()
# print(os.listdir('E:\movies'))
# for i in os.listdir('F:\Python_Programmes\Os modules'):
#     print(r'F:\Python_Programmes\Os modules'+'\\\\------>'+i)
#     path=os.path.join(os.getcwd(),'------> ',i)
#     print(path)
#     path=os.path.join(r'F:\Python_Programmes\Os modules',i) #---this is used for cwd ........ :
#     print(path)