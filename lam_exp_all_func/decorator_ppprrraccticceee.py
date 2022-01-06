# def decorator_func(any_func):
#     def wrapper_func(*args,**kwargs):
#         print('This function take a list and expo of a number :')
#         return any_func(*args,**kwargs)
#     return wrapper_func
# @decorator_func
def func_1(num,*args):
    return[i**num for i in args]
user=int(input('How many number enter in list :'))
print('ENTER ',user,'NUMBER :')
total=[]
for i in range(user):
    num_1=int(input())
    total.append(num_1)
expo=int(input('Enter the expo for all numbers :'))
print(func_1(expo,*total))
input()