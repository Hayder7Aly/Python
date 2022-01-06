def sum_1(*args):
    total=0
    for num in args:
        total+=num
    return total
n=int(input('Enter 1st number:'))
n2=int(input('Enter 2nd number:'))
n3=int(input('Enter 3rd number:'))
print('The sum of all numbers Is:')
print(sum_1(n,n2,n3))
input()