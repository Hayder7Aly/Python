def multiple(n):
    return[i*char for i in n]
user=int(input('How many numbers enter in list :'))
total=[]
print('Enter',user,'numbers :')
for i in range(user):
    nums=int(input())
    total.append(nums)
print(total)
char=int(input('Which char to multiple all enteries :'))
print(multiple(total))
input()