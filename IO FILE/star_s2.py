with open('star_s2.txt','a') as a:
    row=int(input('Enter a number of row :'))
    a.write(f'Your stayle in {row} row is given below\n')
    for i in range(row):
        total=''
        for i in range(row):
            total+='*'
        a.write(f"{total}\n")