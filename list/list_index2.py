user=int(input('How many entery enter in list :'))
print('Enter ',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
char=int(input('Which char print in your list :'))
print(total[char])
input()