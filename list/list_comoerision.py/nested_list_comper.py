user=int(input('How many numbers enter in list :'))
print('Enter',user,'Numbers :')
total=[]
for i in range(user):
    nums=int(input())
    total.append(nums)
print(total)
user2=int(input('How many times you want to copy of your list :'))
list_1=[[i for i in total] for i in range(user2)]
print(list_1)
input()