row=int(input('ENTER THE NUMBER OF ROWS :'))
i=row
while i>=1:
    total=''
    for i in range(row):
        total+='*'
    print(total)
    row=row-1
input()