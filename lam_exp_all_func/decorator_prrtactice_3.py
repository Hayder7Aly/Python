from functools import wraps
def decorator_func(any_func):
    @wraps(any_func)
    def wrapper_func(*args,**kwargs):
        print(f"you are calling {any_func.__name__} function")
        print(f"{any_func.__doc__}")
        return any_func(*args,**kwargs)
    return wrapper_func
@decorator_func
def add(a,b):
    ''' This function takes two argument and return their sum'''
    return a+b
print(add(4,3))
@decorator_func
def substract(a,b):
    ''' This function takes two argument and return their substract'''
    return a-b
print(substract(59,5))
input()