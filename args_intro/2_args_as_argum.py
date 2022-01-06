def sum_number(*args):
    total=0
    for num in args:
        total+=num
    return(total)
user=int(input('How many number enter in programme for addition:'))
print('Enter',user,'Number :')
total=[]
for i in range(user):
    num=int(input()) 
    total.append(num)
print('The sum of all number is :',sum_number(*total) )
input()