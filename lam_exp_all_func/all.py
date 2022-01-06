def numbers(l):
    return all([i%11==0 for i in l])
user=int(input('HOW MANY NUMBER ENTER IN LIST :'))
print('ENTER',user,'NUMBER :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print('IF ALL NUMBER DIVIDED BY 11 PRINT TRUE ELSE FALSE ::')
print(numbers(total))
input()