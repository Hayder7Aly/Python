average_finder=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
user=int(input('How many number enter in 1st list :'))
print('Enter',user,'number')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
user2=int(input('How many number enter in 2nd list :'))
print('Enter',user2,'number')
total2=[]
for i in range(user2):
    num2=int(input())
    total2.append(num2)
print(total)
print(total2)
print(average_finder(total,total2))
input()