whole_number=int(input('Enter a number :'))
total_1=0
total_2=0
for i in range(whole_number+1):
    if i%2==0:
        total_1+=i
    else:
        total_2+=i
print('The sum of all even number :',total_1)
print('The sum of all odd number :',total_2)
input()