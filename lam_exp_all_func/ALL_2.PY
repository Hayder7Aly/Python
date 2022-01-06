user=int(input('How many number enter in list :'))
print('Enter',user,'number :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print(total)
print('\t\tIF USER ENTER EACH NUMBER DIVIDED BY 11 THEN PRINT TRUE ELSE PRINT FALSE :')
print(all([i%11==0 for i in total]))
input()
