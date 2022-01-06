from functools import wraps
import time
def decorator_func(function):
    @wraps(function)
    def wrapper_func(*args,**kwargs):
        t1=time.time()
        print(f'This function name is {function.__name__} function')
        t2=time.time()
        total_time=(t2-t1).__round__(4)
        print(f'This function take total time is {total_time} sec')
        return function(*args,**kwargs)
    return wrapper_func
@decorator_func
def square(*args):
    return [i**2 for i in args ]
square_2=[100000]
print(square(*square_2))
input()
