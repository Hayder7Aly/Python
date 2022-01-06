user=int(input('How many entery enter in list  :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
list1=total
char=input('Enter a string delete in list :')
list1.remove(char)
print(list1)
input()