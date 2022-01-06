def func(a):
    return a**2
l=[1,2,3,4,5]
def my_map(func,l):
    new_list=[]
    for i in l:
        new_list.append(func(i))
    return new_list
print(my_map(func,l))
def my_2_map(func,l):
    return [func(item) for item in l]
print(my_2_map(lambda a: a**3,l))
input()