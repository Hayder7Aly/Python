def odd_even(list_1):
    return[i**2 if i%2==0 else -i for i in list_1]
user=int(input('How many numbers enter in list :'))
print('Enter',user,'Numbers :')
total=[]
for i in range(user):
    numbers=int(input())
    total.append(numbers)
print(total)
print('\tAll even number in list in square :')
print('\tAll odd number in list in negative foarm :')
print(odd_even(total))
input()