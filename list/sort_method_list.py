user=int(input('How many entery enter in list :'))
print('Enter',user,'entery  :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
list1=total
list1.sort()
print(list1)
input()