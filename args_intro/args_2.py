def sum_1(*args):
    total=1
    for num in args:
        total*=num
    return total
n_1=int(input('Enter 1st number:'))
n_2=int(input('Enter 2nd number:'))
n_3=int(input('Enter 3rd number:'))
print('The product of all numbers is :')
print(sum_1(n_1,n_2,n_3))
input()