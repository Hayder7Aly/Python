user=int(input('How many Entery in list :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
list1=total
char=int(input('Which char delete in list in index :'))
del list1[char]
print(list1)
input()

