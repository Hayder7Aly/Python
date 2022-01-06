user=int(input('How many entery enter in dict :'))
total={}
for i in range(user):
    key=input('Enter the key :')
    value=input('Enter the vlaue :')
    total[key]=value
print(total)
print('if you want your dict copy print :')
user=input('Enter yes for copy else enter :')
if user=='yes':
    print(total.copy())
else:
    print('you did not copy dict :')
input()