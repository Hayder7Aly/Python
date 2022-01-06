def number(*args):
    return [i**2 if i%2==0 else i**3 for i in args]
user=int(input('How many number enter in progrmme :'))
print('Enter',user,'Number:')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print('All even number in square foarm and odd number in cube :')
print(number(*total))
input()