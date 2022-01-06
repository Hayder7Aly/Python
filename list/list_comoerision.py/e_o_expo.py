user=int(input('Enter so on number :'))
list_1=[i**2  if i%2==0 else -i**2 for i in range(1,user+1) ]
list_2=[i**3  if i%2==0 else -i**3 for i in range(1,user+1)]
print('\n\t\tAll list enteries of odd numbers in negative form :\n')
print(list_1)
print(list_2)
input()