row=int(input('Enter the number of rows :'))
i=row
while i>=1:
    total=''
    for i in  range(row):
        total+=str(i)
    print(total)
    row=row-1
input()