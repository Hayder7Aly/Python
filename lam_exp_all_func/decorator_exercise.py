import time
t1=time.time()
from functools import wraps
def decorator_func(any_func):
    @wraps(any_func)
    def wrappers_func(*args,**kwargs):
        print(f'You are calling {any_func.__name__} function')
        print(f'{any_func.__doc__}')
        return any_func(*args,**kwargs)
    return wrappers_func
@decorator_func
def function(*l):
    '''This function takes two  a list and return choice able number  and calculate the time'''
    return[i for i in l if i%3==0]
l=[3,4,5,6,9,33]
print(function(*l))
t2=time.time()
print(t2-t1)
input()