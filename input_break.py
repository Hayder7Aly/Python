n=int(input('Enter a number for print :'))
n2=int(input('Enter a number for break :'))
for i in range(1,n+1):
    if i==n2+1:
        break
    print(i)

input()