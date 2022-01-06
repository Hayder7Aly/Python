def odd_even(number):
    return{i:('even' if i%2==0 else 'odd')for i in number}
user=int(input('How many number enter in dict :'))
print('Enter',user,'Number :')
total=[]
for i in range(user):
    num=int(input())
    total.append(num)
print(odd_even(total))
input()
