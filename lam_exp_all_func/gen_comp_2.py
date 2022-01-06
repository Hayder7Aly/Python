def square(l):
    return(i**2 for i in l)
user=int(input('How many number enter in list :'))
print('Enter',user,'Number :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print('SQUARE OF ALL NUMBER WHICH YOU TYPE WITH ACSENDING ORDER :')
square_2=square(total)
for i in square_2:
    print(i)
input()