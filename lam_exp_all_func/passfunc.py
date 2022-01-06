def func(a):
    return a%2==0
user=int(input('How many number enter in list for conditions:'))
print('Enter',user,'numbers:')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
def my_map(func,total):
    new=[]
    for i in total:
        new.append(func(i))
    return new 
print('\t\tIF NUMBER IS EVEN THEN TRUE ELSE FALSE .')
print(my_map(func,total))