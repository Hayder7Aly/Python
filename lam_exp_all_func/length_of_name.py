user=int(input('How many name enter in list :'))
print('Enter',user,'name :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
print('LONGEST NAME IN LIST IS :')
print(max(total,key=lambda item:len(item)))
input()