def names(s):
    return{name[0] for name in s}
user=int(input('Enter how many entery enter in set :'))
print('Enter',user,'Entery :')
total={'s'}
for i in range(user):
    name_1=input()
    name2=name_1.title()
    total.add(name2)
total.remove('s')
print(total)
print('The first char of all element is collected :')
print(names(total))
input()