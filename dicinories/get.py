user=int(input('How many entery enter in dict :'))
total={}
for i in range(user):
    name=input('Enter the key :')
    name2=input('Enter the value :')
    total[name]=name2
print(total)
char=input('which value you want to print enter its key : ')
print(total.get(char))
input()