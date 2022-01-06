def divide(d):
    return[i/char.__round__(3) for i in d]
def multiple(m):
    return[i*char for i in m]
def add(a):
    return[i+char for i in a]
def substract(s):
    return[i-char for i in s]
user=int(input('How many number enter in list :'))
print('Enter',user,'Numbers :')
total=[]
for i in range(user):
    nums=int(input())
    total.append(nums)
print(total)
char=int(input('Enter a char for all operators :'))
print('In division :\n',divide(total))
print('In multiple :\n',multiple(total))
print('In addition :\n',add(total))
print('In substraction :\n',substract(total))
input()