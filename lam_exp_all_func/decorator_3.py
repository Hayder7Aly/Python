from functools import wraps
def decorator_func(any_func):
    @wraps(any_func)
    def wrappper_func(*args,**kwargs):
        '''This is awsome function'''
        return any_func(*args,**kwargs)
    return wrappper_func
@decorator_func
def func(a,b):
    '''This function is add function'''
    return a+b
func(3,5)
print(func.__doc__)
print(func.__name__)
input()