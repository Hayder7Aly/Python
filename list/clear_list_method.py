user=int(input('How many entery  enter in list :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
total.clear()
print('your list is empty :')
print(total)
input()