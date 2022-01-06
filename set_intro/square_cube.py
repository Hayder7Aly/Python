user=int(input('How many number enter in set :'))
total={0}
total_1={0}
total_2={0}
print('Enter',user,'Entery :')
for i in range(user):
    number_1=int(input())
    total.add(number_1)
    total_1.add(number_1**2)
    total_2.add(number_1**3)
total.remove(0)
total_1.remove(0)
total_2.remove(0)
print(total)
print('The square of set is :')
print(total_1)
print('The cube of set is :')
print(total_2)
input()