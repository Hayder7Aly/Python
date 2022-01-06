def number(num,*args):
    if args:
        return[i**num for i in args]
    else:
        return "you did't type args :"
user=int(input('How many number enter in progarmme :'))
print('Enter',user,'Number')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
expo=int(input('Enter exponent for all numbers :'))
print(number(expo,*total))
input()