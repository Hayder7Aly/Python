user=int(input('Enter the number :'))
total=[]
for i in range(user+1):
    total.append(i)
print('your total lsit is  :\n')
print(total)
l3=total
total1=[]
i=0
while i <=user:
    total1.append(i)
    i+=2
print('Even number  list :\n')
print(total1)
list1=total1
i=1
total2=[]
while i <=user:
    total2.append(i)
    i+=2
print('Odd number list :\n')
print(total2)
list2=total2
list1.append(list2)
print('Total list of even and odd number :\n')
print(list1)
input()