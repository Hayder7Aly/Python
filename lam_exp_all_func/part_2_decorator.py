def decorater_func(any_func):
    def wrapper_func(*args,**kwargs):
        print('This is awesome function:')
        return any_func(*args,**kwargs)
    return wrapper_func
@decorater_func
def func(a):
    print('This function with argument :',a)
func(3)
@decorater_func
def func_2(a,b):
    print('This function with argument :')
    return a+b
print(func_2(5,3))
input()