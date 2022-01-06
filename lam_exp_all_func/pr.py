def func(*args):
    total=0
    for i in args:
        if type(i)==int:
            total+=i
        else:
            print(f'Invalid choice :{i}')
    return total
l=[1,2,3,4,[44,5],7,[3,3,4]]
print('sum of all int numbers is :',func(*l))
input()