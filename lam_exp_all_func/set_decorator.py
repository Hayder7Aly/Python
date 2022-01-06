def decorator_func(any_func):
    def wrapper_func(*args,**kwargs):
        print('This function takes set and return those number whose modules is 0 divided by 5 :')
        return any_func(*args,**kwargs)
    return wrapper_func
@decorator_func
def func_1(set_1):
    return{i for i in set_1 if i%5==0 }
user=int(input('HOW MANY NUMBER ENTER IN SET :'))
print('enter',user,'num,ber')
total={0}
for i in range(user):
    num=int(input())
    total.add(num)
total.remove(0)
print(func_1((total)))
input()