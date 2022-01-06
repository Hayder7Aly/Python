print('Enter ten numbers:')
i=1
total=0
while i<=10:
    num=float(input())
    total=total+num
    i+=1

average=total/10
print('sum of 10 number is :',total)
if 20<=average<=40:
    print('average of 10 number is :',average)
else:
    pass
input()