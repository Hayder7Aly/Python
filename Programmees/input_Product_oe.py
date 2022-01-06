user=int(input('How many numbers enter in programme :'))
print('Enter',user,'Numbers :')
total=1
total_1=1
for i in range(1,user+1):
    num=int(input())
    if num%2==0:
        total=total*num
    else:
        total_1=total_1*num
print('The product of all even number is :',total)
print('The product of all odd number is :',total_1)
input()