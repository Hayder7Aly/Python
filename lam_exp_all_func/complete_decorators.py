from functools import wraps
def only_data_type(data_type):
    def decorators(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return function(*args,**kwargs)
            print('Invalid choice :')
        return wrapper
    return decorators
@only_data_type(float)
def list_1(*args):
    total=0
    for i in args:
        total+=i
    return total
l=[2.2,5.3,'haid']
print(list_1(*l))
input()