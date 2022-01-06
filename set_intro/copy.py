user=int(input('How many entery enter in set :'))
total={''}
for i in range(user):
    sets=input()
    total.add(sets)
total.remove('')
print(total)
print('Copy of set is appears :')
total.copy()
print(total)
input()