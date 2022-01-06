user=int(input('How many entery enter in dict :'))
total={}
for i in range(user):
    key=input('Enter the key :')
    value=input('Enter the vlaue :')
    total[key]=value
print(total)
print('if you want your dict empty :')
user=int(input('Enter 1 or other buttons :'))
if user==1:
    print(total.clear())
else:
    print('you did not empty dict :')
input()