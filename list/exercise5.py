user=int(input('Enter the number in 1st list :'))
total=[]
for i in range(user):
    number=int(input())
    total.append(number)
print('your 1st lsit is  :\n')
print(total)
list1=total
user2=int(input('Enter the number in 2nd list :'))
total2=[]
for i in range(user2):
    number2=int(input())
    total2.append(number2)
print('your 2nd list is  :\n')
print(total2)
list2=total2
total3=[]
for i in list1:
    if i in list2:
        total3.append(i)
print('Your common lists items  in list3:\n')
print(total3)
input()