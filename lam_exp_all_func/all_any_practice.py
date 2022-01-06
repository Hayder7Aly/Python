def num_sum(*args):
    if all([type(i)==int or type(i)==float for i in args]):
        total=0
        for i in args:
            total+=i
        return total
    else:
        return 'Wrong input :'
print(num_sum(1,2,3,4,5,3.2,'haider'))
input()