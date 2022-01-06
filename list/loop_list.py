user=int(input('How many entery enter in list :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
user2=int(input('How many character found in list  :'))
print('Enter',user,'found character :')
total2=total
for i in range(user2):
    char=input()
    if char in total2:
        print('present :')
    else:
        print('not present:')
input()