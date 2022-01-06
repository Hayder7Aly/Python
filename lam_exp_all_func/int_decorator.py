from functools import wraps
def decorators_func(function):
    @wraps(function)
    def wrapper_func(*args,**kwargs):
        print(f'This function name is {function.__name__} function')
        print(f'{function.__doc__}')
        if all([type(arg)==int for arg in args]):
            return function(*args,**kwargs)
        print('Invalid argument :')
    return wrapper_func
@decorators_func
def addition(*args):
    '''This function take a list and sum all element in list :'''
    total=0
    for i in args:
        total+=i
    return total
user=int(input('How many number enter in list :'))
print('Enter',user,'num,ber:')
total_1=[]
for i in range(user):
    num=int(input())
    total_1.append(num)
print(addition(*total_1))
input()