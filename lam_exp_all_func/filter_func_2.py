user=int(input('How many number enter in list :'))
print('enter',user,'number :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print(total)
first_char=list(filter(lambda a:a//5>=12,total))
print('\t IF NUMBER IN LIST QUITENT GREATER THAN 12 ARE EQUAL TO 12 FILTER IN NEW LIST :')
print(first_char)
input()