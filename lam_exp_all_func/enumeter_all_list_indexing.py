user=int(input('HOW MANY ENTERY ENTER IN LIST :'))
print('ENTER',user,'ENTERY  :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
for pos,name in enumerate(total):
    print(pos,'-------->',name)
input()