def sum_num(*args):
    if all(type(i)==int for i in args):
        print('Sum of all numbers is :')
        total=0
        for i in args:
            total+=i
        return total
    else:
        return 'Wrong input'
user=int(input('How many number enter in list :'))
print('Enter',user,'number :')
total1=[]
for i in range(user):
    num=int(input())
    total1.append(num)
print(sum_num(*total1))
user2=int(input('How many string create in new list :'))
print('Enter',user,'string :')
string_list=[]
for i in range(user2):
    string_1=input()
    string_list.append(string_1)
choice=input('You want to join the both list Enter yes else enter:')
if choice=='yes':
    total1.extend(string_list)
    print(sum_num(*total1))
input()

