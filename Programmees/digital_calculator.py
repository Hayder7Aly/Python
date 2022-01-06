print('\n\n\t\t===Digital_calculator===')
print('\t1. Press addition for addition :')
print('\t2. Press substraction for sustraction :')
print('\t3. Press division for division :')
print('\t4. Press multiplication for multiplicaton :')
print('\t5. Press g\s for greater_smaler :')
print('\t6. Press o\e for odd_even :')
print('\t7. Press close for close the programme :\n\n')
while True:
    user=input('\nEnter in these following :')
    if user=='7' or user=='close':
        print('Your programme is close :')
        break
    n=float(input('\nEnter 1st number :'))
    n2=float(input('\nEnter 2nd number :'))
    if user=='1' or user== 'addition':
        print('The sum of ',n,'and',n2,'is: ',n+n2)
    elif user=='2' or user=='substraction':
        print('The substraction of ',n,'and',n2,'is: ',n-n2)
    elif user=='3' or user=='division':
        print('The division of number ',n,'/',n2,'is :',n/n2)
    elif user=='4' or user=='multiplication':
        print('The Multiplication of',n,'and',n2,'is :',n*n2)
    elif user=='5' or user=='g\s':
        if n>n2:
            print('Greater number is :',n)
            print('Smaller number is :',n2)
        elif n2>n:
            print('Greater number is :',n2)
            print('Smaller number is :',n)
        else:
            print('Both equal numberS :')
    elif user=='6' or user=='o\e':
        if (n%2==0) and (n2%2==0):
            print('Both numbers are Even numbers :')
        elif (n%2==0):
            print('Even number is :',n)
            print('Odd number is :',n2)
        elif (n2%2==0):
            print('Even number is :',n2)
            print('Odd number is :',n)
        else:
            print('Both numbers are Odd numbes :')
input()