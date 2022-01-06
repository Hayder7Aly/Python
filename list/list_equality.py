user=int(input('How many entery enter in list :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
list1=total
user2=int(input('How many entery enter in list :'))
print('Enter',user2,'entery :')
total2=[]
for i in range(user2):
    name2=input()
    total2.append(name2)
print(total2)
list2=total2
if list1==list2:
    print('Lists are same :')
else:
    print('Not same list :')
input()