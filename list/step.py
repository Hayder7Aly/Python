user=int(input('How many entry enter in list :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
char=int(input('Enter step arrgument :'))
print(total[::char])
input()