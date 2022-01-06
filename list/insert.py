user=int(input('How many entery in list :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
char=int(input('Enter insert char in index :'))
string=input('Enter string  insert in list :')
total.insert(char,string)
print(total)
input()