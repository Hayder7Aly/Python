user=int(input('How many number enter in list :'))
print('Enter',user,'Number :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print(total)
new_even=list(filter(lambda a:a%2==0,total))
print('ALL EVEN NUMBER FILTER IN NEW LIST :')
print(new_even)
input()