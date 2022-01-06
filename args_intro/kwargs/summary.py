# *args
def func(*args):
    return args
l=[1,2,3,4]
print(func(*l))
# **KWARGS
def func_1(**kwargs):
    print(kwargs)
func_1(first_name='haider',last_name='ali')
def func_2(**kwargs):
    print(kwargs)
d={'name':'haider','age':15}
func_2(**d)
# PADK
def user_info(name,*args,last_name='jutt007',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
user_info('haider',1,2,3,a=1,b=2)
input()