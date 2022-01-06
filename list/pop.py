user=int(input('How many entery enter in list :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
list1=total
index=int(input('Enter delete char in list  in index:'))
list1.pop(index)
print(list1)