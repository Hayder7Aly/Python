user=int(input('How many entery enter in sets :'))
total={''}
print('Enter',user,'entery :')
for i in range(user):
    sets=input()
    total.add(sets)
total.remove('')
print(total)
for i in total:
    print(i)
input()