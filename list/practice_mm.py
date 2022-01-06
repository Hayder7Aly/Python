# name=['jutt','haider','ali']
# print(min(name))
# print(max(name))
user=int(input('How many entery enter in list :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
print('Maximum name is :')
print(max(total))
print('mininun name is :')
print(min(total))
input()