def func(**kwargs):
    return kwargs
print(func(first_name='haider',last_name='ali'))
def func_1(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,' : ',v)
d={'name':'haider','age':24}
func_1(**d)
input()
