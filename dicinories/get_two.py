user=int(input('How many entery enter in dict :'))
total={}
for i in range(user):
    keys=input('Enter the key of dict :')
    value=input('Enter the value of key :')
    total[keys]=value
print(total)
char=input('Enter your char in founded in dict :')
if total.get(char):
    print('Present ')
else:
    print('Not Present')
input()