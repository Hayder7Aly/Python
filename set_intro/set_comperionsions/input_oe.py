def oe(s):
    return{i if i%2==0 else -i for i in s}
user=int(input('How many number enter in set:'))
print('Enter',user,'number')
total={0}
for i in range(user):
    num=int(input())
    total.add(num)
total.remove(0)
print('even number is possitive and odd number is negative :')
print(oe(total))
input()