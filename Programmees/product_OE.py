number=int(input('Enter a number :'))
total_1=1
total_2=1
for i in range(1,number+1):
    if i%2==0:
        total_1=total_1*i
    else:
        total_2=total_2*i
print('The product of all even number is :',total_1)
print('The product of all odd number is :',total_2)
input()