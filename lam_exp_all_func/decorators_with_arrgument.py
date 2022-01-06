from functools import wraps
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            print(f'THIS data type name is {data_type.__name__} data type :')
            print(f'{function.__doc__}')
            if all([type(arg)==data_type for arg in args]):
                return function(*args,**kwargs)
            print('Invalid arrgument:')
        return wrapper
    return decorator
@only_data_type_allow(str)
def func(*args):
    '''This fucntion takes list of string and return concatination'''
    string=''
    for i in args:
        string+=i
    return string  
user=int(input('How many name enter in list :'))
print('Enter',user,'name:')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(func(*total))