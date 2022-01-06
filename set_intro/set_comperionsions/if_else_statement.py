user=int(input('Enter the range of number:'))
comp={i**2 if i%2==0 else i**3 for i in range(1,user+1)}
print('All even number in square and odd number in cube :')
print(comp)
input()