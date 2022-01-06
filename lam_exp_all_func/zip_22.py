l=lambda *args:[sum(pair)**2 for pair in zip(*args)]
user=int(input('HOW MANY NUMBER ENTER IN 1ST LIST :'))
print('ENTER',user,'NUMBE :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print(total)
user_2=int(input('HOW MANY NUMBER ENTER IN 2ND LIST :'))
print('ENTER',user_2,'NUMBER :')
total_2=[]
for  i in range(user_2):
    num_2=int(input())
    total_2.append(num_2)
print(total)
print(total_2)
print('\t\tBOTH LIST COROSPONDING ENTERIES SUM AND TAKE SQUARE :')
print(l(total,total_2))
input()