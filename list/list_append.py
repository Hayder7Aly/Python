user=int(input('How many entery enter in list :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
char=int(input('Which char to start print in index 0  :'))
char2=int(input('Which char to stop print in index +1  :'))
char3=int(input('Enter step arrgument up 0  :'))
print(total[char:char2:char3])
input()