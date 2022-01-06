name=input('Enter your name/string :')
temp_var=''
for i in range(len(name)):
    if name[i] not in temp_var :
        temp_var+=name[i]
        print(name[i],':',name.count(name[i])) 

input()    