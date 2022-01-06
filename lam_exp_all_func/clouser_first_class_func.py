def expo(x):
    def number(n):
        return n**x
    return number
square=expo(2)
print(square(4))
cube=expo(3)
print(cube(4))
input()