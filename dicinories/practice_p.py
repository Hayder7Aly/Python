user=int(input('How many entery enter in dict :\n'))
print('Enter',user,'Entery :\n')
total={}
for i in range(user):
    name=input('Enter the key of dict :\n')
    name2=input('Enter the value of key :\n')
    total[name]=name2
print(total)
user2=int(input('How many entery enter in dict and update :\n'))
print('Enter',user2,'entery :\n')
total2={}
for i in range(user2):
    name_1=input('Enter the key of dict :\n')
    name_2=input('Enter the value of key :\n')
    total2[name_1]=name_2
total.update(total2)
print('The updation of dict is completed :\n')
print(total)
user3=int(input('How many entery delete in dict :\n'))
print('Enter',user3,'entery :\n')
for i in range(user3):
    name=input('Enter the key of dict :\n')
    total.pop(name)
print(total)
print('The type of data structre is :\n')
print(type(total))
print('\nIf you want to dict in tupple :\nPress yes else enter:\n')
user=input('Enter yes/no :')
if user=='yes':
    print('You chose the tupple :')
    for i in total.items():
        print(i)
else:
    print("You can't chose the tupple:")
print('The key and its value are  in string :\n')
for i,j in total.items():
    print(i,' : ',j)
input()