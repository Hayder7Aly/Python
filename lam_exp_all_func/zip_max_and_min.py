user=int(input('How many number enter in 1st list :'))
print('Enter',user,'number')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
l1=total
print('Enter',user,'number')
total2=[]
for i in range(user):
    num=int(input())
    total2.append(num)
l2=total2
max_1=[]
for pair in zip(l1,l2):
    max_1.append(max(pair))
print('BIGGER LIST IS  :\t\t')
print(max_1)
input()
