user=int(input('HOW MANY NAME ENTER IN SET :'))
print('Enter',user,'name :')
total={''}
for i in range(user):
    name=input()
    total.add(name)
total.remove('')
print(total)
for pos,name_1 in enumerate(total):
    print(pos,'--------->',name_1)
input()