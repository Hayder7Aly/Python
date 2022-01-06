def nums(num,*args):
    print(num)
    print(args)
    muliply=1
    for num in args:
        muliply*=num
    return muliply
print(nums(5,3,4,1,2))
input()
# n=int(input('Enter 1st number :'))
# n2=int(input('Enter 2nd number :'))
# n3=int(input('Enter 3rd number :'))
