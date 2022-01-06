with open('add.txt','a') as a:
    a.write(f'\ngiven statement!\n')
    num=int(input('Enter 1st number :'))
    a.write(f'First number is : {num}\n')
    num2=int(input('Enter 2nd numbe :'))
    a.write(f'Second number is : {num2}\n')
    num3=num+num2
    a.write(f'Sum of both number is : {num3}\n')
