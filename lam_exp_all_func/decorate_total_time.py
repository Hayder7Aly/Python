from functools import wraps
import time 
def decorator_func(function):
    @wraps(function)
    def wrapper_func(*args,**kwargs):
        t1=time.time()
        return_value=function(*args,**kwargs)
        print(f"Your function name is {function.__name__} function")
        print(f"{function.__doc__}")
        t2=time.time()
        total_time=(t2-t1).__round__(7)
        print(f'Total time takes this function is {total_time} sec')
        return return_value
    return wrapper_func
@decorator_func
def expo(*args):
    '''This function takes the list and expo is 100'''
    return [i**10000 for i in args]
user=int(input('How many number enter in list :'))
print('Enter',user,'number :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
expo(*total)
input()