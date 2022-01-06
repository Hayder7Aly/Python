user=int(input('HOW MANY NUMBER ENTER IN LIST :'))
print('ENTER',user,'NUMBER :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print(total)
l_2=set(filter(lambda a : a%7==0,total))
print(l_2)