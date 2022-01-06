user=int(input('How many entery enter in list :'))
print('Enter',user,'entery :')
total=[]
for i in range(1,user+1):
    name=input()
    total.append(name)
print(total)
list1=total
user2=int(input('How many entery insert in first list :'))
for i in range(user2):
    name2=input()
    list1.insert(0,name2)
print(list1)
user3=int(input('How many entery enter in list 2   :'))
print('Enter',user,'entery :')
total1=[]
for i in range(user3):
    name3=input()
    total1.append(name3)
print(total1)
list2=total1
print('both list are extend  :\n')
list1.extend(list2)
print(list1)
input()

