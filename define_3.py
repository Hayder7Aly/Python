def add(a):
    return a
def average(a):
    return (a/5).__round__(4)
def percentage(a):
    return (a*100/500).__round__(4)
print('Enter 5 books marks :')
total=0
for i in range(5):
    numbers=float(input())
    total+=numbers
print('Total marks is :',add(total))
print('Average of marks is :',average(total))
print('Percentage of marks is :',percentage(total))