print('Enter ten numbers:')
i=1
total=1
while i<=10:
    num=float(input())
    total=total+num
    total2=total*num
    total3=(total-1)/10

    i+=1
print('sum of 10 number is :',total-1)
print('product of 10 number is :',total2)
print('average of 10 number is :',total3)
input()