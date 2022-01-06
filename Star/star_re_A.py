row=int(input('Enter the number of rows :'))
i=row
while i>=1:
    total=''
    for i in range(row):
        total+='A****A'
    print(total)
    row=row-1
input()