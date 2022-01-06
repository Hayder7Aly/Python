def odd_even(list_1):
    return[i for i in list_1 if i%2==0 ]
def odd_even_2(list_2):
    return[i for i in list_2 if i%2!=0]
user=int(input('How many numbers enter in list :'))
print('Enter',user,'numbers')
total=[]
for i in range(user):
    numbers=int(input())
    total.append(numbers)
print(total)
print('all even numbers in list :')
print(odd_even(total))
print('all odd numbers in list :')
print(odd_even_2(total))
input()