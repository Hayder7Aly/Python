a=7#global variables
def fun():
    global a
    a=5#local variables 
    return a
print(a)
print(fun())
print(a)
input()