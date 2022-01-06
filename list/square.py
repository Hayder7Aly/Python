user=int(input('How many number enter in list :'))
print('Enter',user,'numbers :')
total=[]
for i in range(user):
    num=int(input())
    num2=num*num
    total.append(num2)
print(total)
input()
