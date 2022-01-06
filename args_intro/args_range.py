def number(*args):
    return [i**2 if i%2==0 else i**3 for i in args]
user=int(input('Enter the so on number:'))
number_ranger=range(1,user+1)
print(number(*number_ranger))
input()