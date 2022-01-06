user=int(input('How many name enter in list:'))
print('Enter',user,'name :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
length=list(map(len,total))
print(length)
input()