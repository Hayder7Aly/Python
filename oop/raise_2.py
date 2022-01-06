def multiple(a,b):
    if type(a)==int and type(b)==int:
        return a-b
    raise ValueError('You have enter wrong data')
print(multiple(3,'a'))
input()