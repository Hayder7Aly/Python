def func(n):
    for i in range(1,n+1):
        yield(i)

for number in func(10):
    print(number)
for number in func(10):   
    print(number)
# Generator can store data in memory ----->  fix and and run same code then its over write same first code :
input()