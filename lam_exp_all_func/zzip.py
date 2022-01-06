l=lambda *args:[sum(pair)**3 for pair in zip(*args)]
user=int(input('HOW MANY NUMBER ENTER IN 1ST LIST :'))
print('ENTER',user,'NUMBER :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print(total)
user_1=int(input('HOW MANY NUMBER ENTER IN 2ND LIST :'))
print('ENTER',user_1,'number:')
total1=[]
for i in range(user_1):
    num_1=int(input())
    total1.append(num_1)
print(total)
print(total1)
print('cubes:')
print(l(total,total1))
input()