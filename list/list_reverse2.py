user=int(input('How many entry enter in list :'))
print('Enter', user ,'entry :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
print('your list is reverse mode :')
print(total[::-1])
input()