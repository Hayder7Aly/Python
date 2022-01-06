def func_1(*args):
    return[i.title() for i in args]
def func_2(*args):
    return[i[::-1].title() for i in args]
user=int(input('How many name enter in list :'))
print('Enter',user,'name :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(func_1(*total))
print(func_2(*total))
input()