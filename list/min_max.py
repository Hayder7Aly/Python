user=int(input('How many entery in numbers in list :'))
print('Enter',user,'numbers')
total=[]
for i in range(user):
    n=int(input())
    total.append(n)
print(total)
print('Minimum number in list :')
print(min(total))
print('maximum number in list :')
print(max(total))
input()