from functools import wraps
def decorator_func(function):
    @wraps(function)
    def wrapper_func(*args,**kwargs):
        print(f"This function name is {function.__name__}")
        print(function.__doc__)
        return function(*args,**kwargs)
    return wrapper_func
@decorator_func
def oepn_func(*args):
    '''This function takes a list and return odd in negative and even in possitive :'''
    return [i if i%2==0 else -i for i in args]
user=int(input('HOW MANY NUMBER ENTER IN LIST  :'))
total=[]
print('Enter',user,'number :')
for i in range(user):
    num=int(input())
    total.append(num)
print(oepn_func(*total))