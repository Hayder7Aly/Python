def numbers(n):
    return[i+i+i for i in n]
user=int(input('How many numbers enter in lisT:'))
total=[]
for i in range(user):
    nums=int(input())
    total.append(nums)
print([total,total,total])
print('All enteries of list are added with corosponding enteries :')
print('\n',numbers(total))
input()


