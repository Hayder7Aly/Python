def sum_1(n):
    return[i+i for i in n ]
user=int(input('How many Number enter in list :'))
total=[]
print('Enter',user,'Number :')
for i in range(user):
    nums=int(input())
    total.append(nums)
print(total)
print('sum of all numbers with itself :\n')
print(sum_1(total))
input()
