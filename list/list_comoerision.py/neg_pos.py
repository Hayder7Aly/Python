user=int(input('How many numbers enter in list :'))
print('Enter',user,'numbers')
total=[]
for i in range(user):
    nums=int(input())
    total.append(nums)
list_1=[i for i in total if i>=0 ]
list_2=[i for i in total if i<0]
print(list_1)
print(list_2)
input()