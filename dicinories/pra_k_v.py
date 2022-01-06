user=int(input('How many entery enter in dict :'))
print('Enter',user,'entery :')
total={}
for i in range(user):
    name=input('Enter the key of dict :')
    name2=input('Enter the value of key :')
    total[name]=name2
print(total)
print('The key and its value are in string :')
for i,j in total.items():
    print(i,' : ',j)
input()