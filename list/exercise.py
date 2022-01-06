
user=int(input('How many enter number in list :'))
print('Enter',user,'numbers')
total=[]
total2=[]
for i in range(user):
    num=int(input())
    num2=num*num
    total2.append(num2)
    total.append(num)
print(total)
print('Square list of 1st list is  :\n',total2)
input()