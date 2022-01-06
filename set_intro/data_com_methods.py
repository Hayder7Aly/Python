user=int(input('How many entery enter in set :'))
total={''}
for i in range(user):
    sets=input()
    total.add(sets)
total.remove('')
print(total)
user2=int(input('How many character delete in sets :'))
for i in range(user2):
    delete=input()
    total.discard(delete)
print(total)
print('\n\tif you want to clear the set enter yes :')
press=input('\nEnter yes/no :')
if press=='yes':
    total.clear()
    print(total)
else:
    print('\nYou did not clear the sets :')
input()