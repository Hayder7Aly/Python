def add(a):
    return a
def average(a):
    return a/user
def percentage(a):
    return a*100/500
user=int(input('How many books number add in programme :'))
print('Enter ',user,'books marks :')
total=0
i=1
while i <=user:
    n=float(input())
    total+=n
    i+=1
print('Sum of number is :',add(total))
print('Average of number is :',average(total))
print('Percentage of number is :',percentage(total))