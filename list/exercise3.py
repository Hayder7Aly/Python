user=int(input('How many entery enter in list :'))
print('Enter',user,'entery :')
total=[]
total2=[]
for i in range(user):
    name=input()
    total.append(name)
    total2.append(name[::-1])
print(total)
print('your list string are reverse :\n\n')
print(total2)
input()