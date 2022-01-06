def decorater_func(any_func):
    def wrapper_func():
        print('This is largest function:')
        any_func()
    return wrapper_func
@decorater_func
def func1():
    print('This is function 1')
func1()
@decorater_func
def func2():
    print('This is function 2')
func2()
input()
# var=decorater_func(func1)
# var()