user=int(input('How many entery enter in dict :'))
print('Enter',user,'Entery :\n')
total={}
for i in range(user):
    name=input('Enter the key of dict :\n')
    name2=input('Enter the value of key :\n')
    total[name]=name2
print(total)
user2=int(input('How many entery enter in dict  and update :\n'))
print('Enter',user2,'Entery :')
total2={}
for i in range(user2):
    name_1=input('Enter the key of dict :\n')
    name_2=input('Enter the value of key :\n')
    total2[name_1]=name_2
total.update(total2)
print('Updation of dict is completed :\n')
print(total)
dic=total
user3=int(input('How many key and its value delete in dict :'))
print('Enter',user3,'Entery :\n')
for i in range(user3):
    name_3=input('Enter the key of dict :\n')
    dic.pop(name_3)
print('Delte of items is completed :\n')
print(dic)
input()



