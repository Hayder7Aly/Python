user=int(input('How many entery enter in dicinory :'))
print('Enter',user,'enter')
total={}
for i in range(user):
    name=input('Enter the key for dicinory :')
    name2=input('Enter the value of key :')
    total[name]=name2
print(total)
user2=int(input('Enter the number how many times you want to delete:'))
for i in range(user2):
    name3=input('Enter the key you want to delete :')
    print(total.pop(name3))
print(total)
input()