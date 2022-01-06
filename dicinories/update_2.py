user=int(input('How many entery enter in dicinory :'))
print('Enter',user,'entery :\n')
total={}
for i in range(user):
    name=input('Enter the key of name :\n')
    name2=input('Enter the value of key :\n')
    total[name]=name2
user_info=total
print(total)
user2=int(input('How many entery enter in dicinory for updation  :')) 
print('Enter',user2,'entery :\n')     
total2={}
for i in range(user2):
    name_1=input('Enter the key of name :\n')
    name_2=input('Enter the value of name :\n')
    total2[name_1]=name_2
more_info=total2
print(total2)
print('Updation of  dicionary is :')
user_info.update(more_info)
print(user_info)
input()
