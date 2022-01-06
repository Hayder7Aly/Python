l=lambda *args:[sum(pair) for pair in zip(*args)]
user=int(input('How many number enter in 1st row matrix :'))
print('Enter',user,'number :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print('FIRST ROW MATRICS IS :')
print(total)
user2=int(input('How many number enter in 2nd row matrix :'))
print('Enter',user2,'number :')
total2=[]
for i in range(user2):
    num2=int(input())
    total2.append(num2)
print('SECOND  ROW  MATRIX IS :')
print(total2)
print('SUM OF TWO ROW MATRIX IS :')
print(l(total,total2))
input()