user=int(input('How many number enter in list :'))
print('Enter',user,'number :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print(total)
print('\t\tIF ONE NUMBER IN LIST DIVIDED BY 7 PRINT TRUE ELSE PRINT FALSE :')
print(any([i%7==0 for i in total]))
input()