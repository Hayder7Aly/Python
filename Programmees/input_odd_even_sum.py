user=int(input('How many numbers enter in programme :'))
print('Enter',user,'Numbers :')
total_1=0
total_2=0
for i in range(user):
    num=int(input())
    if num%2==0:
        total_1+=num
    else:
        total_2+=num
print('The sum of all even numbers is:',total_1)
print('The sum of all odd numbers is :',total_2)
input()