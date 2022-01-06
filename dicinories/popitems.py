user=int(input('How many entery enter in dicinory :'))
print('Enter',user,'enter')
total={}
for i in range(user):
    name=input('Enter the key for dicinory :')
    name2=input('Enter the value of key :')
    total[name]=name2
print(total)
print('last key and value are ramove from dicionary :')
print(total.popitem())
print(total)
input()