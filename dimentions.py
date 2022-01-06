
user=int(input('How many number enter :'))
print('Enter',user,'number :')
total=0
total1=0
for i in range(user):
    num=int(input('Enter positive and negative integers :'))
    if num>=0:
        total+=num
    else:
        total1+=num
print('The sum of possitive number is :',total)
print('The sum of negative number is :',total1)
input()