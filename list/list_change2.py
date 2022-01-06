user=int(input('How many name enter in list :'))
print('Enter name :',user)
total=[]
for i in range(user):
    name=input()
    total.append(name)
name2=total
change=int(input('Enter change  char in index : '))
char=input('Enter char in list :')
name2[change]=char
print(name2)
input()

