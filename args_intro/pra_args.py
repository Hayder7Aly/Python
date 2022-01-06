def odd_even(*args):
    return[i**2 if i%2==0 else i**3 for i in args]
num=range(1,11)
print(odd_even(*num))
input()