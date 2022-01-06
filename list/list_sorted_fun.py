user=int(input('How many entery enter in list :'))
print('Enter',user,'entery  :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
print('List in alphabetical ordered :\n\n')
list1=total
print(sorted(list1))
input()