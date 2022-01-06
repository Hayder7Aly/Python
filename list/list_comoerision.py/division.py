def divided(n):
    return[i/char.__round__(2)  for i in n]
user=int(input('How many numbers enter in list :'))
print('Enter',user,'Numbers :')
total=[]
for i in range(user):
    nums=float(input())
    total.append(nums)
print(total)
char=int(input('Enter a char do you want to divided each enteries :'))
print('All enteries are divide by :',char)
print(divided(total))
input()