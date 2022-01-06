def to_power(x):
    def number(n):
        return n**x
    return number
num=int(input('Enter the number:'))
square=to_power(2)
print(square(num))
cube= to_power(3)
print(cube(num))
input()