user=int(input('Enter the range of dict :'))
odd_even={i:('even' if i%2==0 else 'odd')for i in range(1,user+1)}
print(odd_even)
input()