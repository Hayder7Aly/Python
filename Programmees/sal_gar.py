salary=float(input('Enter your salary :'))
grade=float(input('Enter your grade :'))
if 0<grade<=15:
    salary_2=(25/100)*salary
    print('Your salary is Rs.',salary+salary_2)
if 15<grade<=22:
    salary_3=(50/100)*salary
    print('Your salary is Rs.',salary+salary_3)
else:
    print('Invalid choice :')
input()