user=int(input('How many entery enter in lists :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
list1=total
print('ALL NAME IN ALPHABETICAL ORDER AND LIST TO STRING  :\n\n\n')
print('\n'.join(sorted(list1)))
input()