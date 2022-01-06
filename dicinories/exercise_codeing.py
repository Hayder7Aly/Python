user=int(input('How many entery enter in dict :'))
total={}
for i in range(user):
    keys=input('Enter your keys :')
    values=input('Enter your values :')
    total[keys]=values
print(total)
for keys,values in total.items():
    print(keys,':',values)
input()