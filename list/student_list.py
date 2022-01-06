user=int(input('How many students name enter in list :'))
print('Enter ',user,'students name :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
print('Student name in alphabetical order :\n')
total.sort()
print(total)
input()