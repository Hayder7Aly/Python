def add(a,b):
    if type(a) is int and type (b) is int:
        return a+b
    raise ValueError("Your have enter wrong data ")

print(add(3,'a'))
input()