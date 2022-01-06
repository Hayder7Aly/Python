with open('store_calculation.txt','a') as a:
    one=int(input('Enter first number :'))
    two=int(input('Enter second numbe :'))
    three=one+two
    a.write(f'Sum of {one} and {two} is :{three}\n')
    a.close()