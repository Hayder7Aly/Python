n=int(input('Enter the number for print :'))
n2=int(input('Enter the number skip in print number :'))
for i in range(1,n+1):
    if i==n2:
        continue
    print(i)

input()    