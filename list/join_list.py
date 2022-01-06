user=int(input('How many entery enter in lists :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
list1=total
print('ALL NAME IN  LIST TO STRING  :\n\n')
print('\n'.join(list1))
input()
