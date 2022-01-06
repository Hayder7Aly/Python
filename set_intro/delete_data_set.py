user=int(input('How many entery enter in set :'))
total={''}
for i in range(user):
    sets=input()
    total.add(sets)
total.remove('')
print(total)
user=int(input('How many set character delete in sets :'))
for i in range(user):
    delete=input()
    total.discard(delete)
print(total)
input()