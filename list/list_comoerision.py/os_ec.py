def odd_even(l):
    return[i**3 if i%2==0 else i**2 for i in l]
range_1=int(input('Enter the range of natural number :'))
list_1=list(range(1,range_1+1))
print('All Odd number in square and Even number in cube:')
print(odd_even(list_1))
input()