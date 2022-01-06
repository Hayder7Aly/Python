user=int(input('How many entery enter in set :'))
total={''}
for i in range(user):
    sets=input()
    total.add(sets)
total.remove('')
print(total)
print('Your set is empty :')
total.clear()
print(total)
input()