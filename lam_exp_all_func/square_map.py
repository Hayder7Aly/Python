user=int(input('How many number enter in list :'))
print('Enter',user,'Number :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print(total)
squares=list(map(lambda a :a**2 ,total))
print(squares)
input()