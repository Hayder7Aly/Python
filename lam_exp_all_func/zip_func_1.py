user=int(input('Hwo many name enter in 1st list :'))
print('Enter',user,'name:')
total=[]
for i in range(user):
    name=input()
    total.append(name)
list_1=total
user_1=int(input('Hwo many name enter in 2nd list :'))
print('Enter',user_1,'Name :')
total_1=[]
for i in range(user_1):
    name_1=input()
    total_1.append(name_1)
list_2=total_1
dict_1=dict(zip(total,total_1))
print(dict_1)
input()