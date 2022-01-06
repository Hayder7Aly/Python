with open('table.txt','a') as a:
    data=int(input('Enter a table numbe :'))
    a.write(f'Table of {data} is given below :\n')
    for i in range(1,11):
        num=f"{data} * {i} = {data*i}\n"
        a.write(num)