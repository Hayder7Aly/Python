user=int(input('How many entery enter in list :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
list1=total
char=input('Enter char locate in list :')
if char in list1:
    print('This char is present :',char)
else:
    print('This char is not present :',char)
input()