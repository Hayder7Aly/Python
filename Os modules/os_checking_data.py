import os
path1=input('Enter a path in which you check data :')
if not os.path.exists(path1):
    print('Please enter corect path :')
else:
    for item in os.listdir(path1):
        print(path1,'--->',item)
input()