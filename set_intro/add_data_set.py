user=int(input('How many entery enter in set :'))
total={''}
for i in range(user):
    sets=input()
    total.add(sets)
total.remove('')
print(total)
input()