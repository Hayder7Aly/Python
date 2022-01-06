def num(*args):
    multiply =1
    for num in args:
        multiply*=num
    return multiply
num_1=[2,3,4]
print(num(*num_1))
input()