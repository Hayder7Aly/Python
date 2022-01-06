def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def divide(a,b):
    return (a/b).__round__(4)
def multiple(a,b):
    return a*b
num=float(input('Enter 1st number :'))
num2=float(input('Enter 2nd number :'))
print('\nThe Addition of',num,'and',num2,'is :\nAnswer =',add(num,num2))
print('\nThe Substraction of',num,'and',num2,'is :\nAnswer =',substract(num,num2))
print('\nThe Division of',num,'/',num2,'is :\nAnswer=',divide(num,num2))
print('\nThe Multiplication of',num,'and',num2,'is :\nAnswer =',multiple(num,num2))
input()
