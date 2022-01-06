def multiply_number(*args):
    multiply=1
    for i in args:
        multiply*=i
    return multiply
user=int(input('How many number enter in programme for product :'))
print('Enter',user,'Number:')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print('The product of all number is :',multiply_number(*total))