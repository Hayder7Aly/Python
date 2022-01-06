user=int(input('How many numbers enter in list :'))
print('Enter',user,'Numbers :')
total=[]
for i in range(user):
    nums=int(input())
    total.append(nums)
print(total)
print('The list of Even numbers :')
list_1=[i for i in total if i%2==0]
print(list_1)
print('The list of odd numbers :')
lsit_2=[i for i in total if i%2!=0]
print(lsit_2)
input()