def num(*args):
    print(type(args))
    return args
print(num(1,2,3,4,5))
def sum(*args):
    total=0
    for num in args:
        total+=num
    return total
print(sum(1,2,3,4,5))
input()