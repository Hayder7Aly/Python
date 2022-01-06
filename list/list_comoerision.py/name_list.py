user=int(input('How many names enter in list :'))
print('Enter',user,'Names :')
total=[]
for i in range(user):
    name=input()
    name2=name.title()
    total.append(name2)
print(total)
list_1=[name[0] for name in total]
print(list_1)
input()