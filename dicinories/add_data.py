user=int(input('How many entery enter in dicinory :'))
print('Enter',user,'entery :')
total={}
for i in range(user):
    name=input('Enter the key value :')
    name2=input('Enter the value of key :')
    total[name]=name2
print(total)
input()
