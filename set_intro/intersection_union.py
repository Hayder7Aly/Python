user=int(input('How many numbers enter in first sets :'))
total={0}
print('ENTER',user,'ENTERY :')
for i in range(user):
    num=int(input())
    total.add(num)
total.remove(0)
print(total)
user2=int(input('How many numbers enter in second sets :'))
total2={0}
print('ENTER',user2,'ENTERY :')
for i in range(user2):
    num2=int(input())
    total2.add(num2)
total2.remove(0)
print(total2)
print('\n\t\tTHE UNION OF TWO SETS IS :',total|total2)
print('\n\t\tTHE INTERSECTION OF TWO SETS IS :',total&total2)
input()