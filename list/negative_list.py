user=int(input('How many number enter in list :'))
print('Enter',user,'numbers :')
total=[]
total2=[]
for i in range(user):
    number=int(input())
    total2.append(number)
    total.append(-number)
print(total2)
print('Your list in negative mode :')
print(total)
input()