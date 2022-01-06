def numbers(n):
    return[str(i) for i in n if type(i)==int or type(i)==float or type(i)==list ]
print(numbers([1,2,3,[1,2,3],'haider',2.2]))
input()    