def decorater_func(any_func):
    def wrapper_func(*args,**kwargs):
        print('This function takes a number and return which number divided by 11 and % number is 0 and other nmber count in square  :')
        return any_func(*args,**kwargs)
    return wrapper_func
@decorater_func
def func(list_1):
    return [i if i%11==0 else i**2 for i in list_1]
user=int(input('How many number enter in list :'))
print('Enter',user,'number ;')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print(func(total))
input()