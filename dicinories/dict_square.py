user=int(input('How many number enter in dict :'))
print('Enter',user,'numbers :\n')
total={}
total2={}
for i in range(user):
    num=input('Enter the key of dict :\n')
    num2=int(input('Enter the value of dict :\n'))
    num3=num2*num2
    total2[num]=num3
    total[num]=num2
print(total)
print('Square of dict is :')
print(total2)
input()