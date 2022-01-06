def func(a,b):
    add=a+b
    multiple=a*b
    return add,multiple
n=int(input('Enter 1st number :'))
n2=int(input('Enter 2nd number :'))
print('first element is addition other is multiplication :')
print(func(n,n2))
input()