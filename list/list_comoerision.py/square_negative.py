user=int(input('How many numbers enter in list :'))
print('Enter',user,'numbers :')
total=[]
for i in range(user):
    nums=int(input())
    total.append(nums)
print(total)
list_1=[i**2 if(i%2==0) else -i for i in total]
print(list_1)
input()