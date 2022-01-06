user=int(input('How many numbers enter in list : '))
print('Enter',user,'Numbers :')
total=[]
for i in range(user):
    nums=float(input())
    total.append(nums)
print(total)
list_1=[str(i) for i in total if(type(i)==int or type(i)==float)]
print(list_1)
input()