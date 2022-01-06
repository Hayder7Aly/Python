user=int(input('HOW MANY NUMBER ENTER IN 1ST LIST :'))
print('Enter',user,'number :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print('\t\tALL NUMBER ADDED IN NEW_LIST WHICH DIVIDED BY 11 :')
print(list(filter(lambda a: a%11==0,total)))
input()