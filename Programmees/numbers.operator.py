num_1=float(input('Enter 1st number :'))
print('+,-,*,/ used this operator :')
operator=input('Enter operator between two numbers  :')
num_2=float(input('Enter 2nd number:'))
if operator=='+':
    print('Answer =',num_1+num_2)
elif operator=='-':
    print('Answer =',num_1-num_2)
elif operator=='*':
    print('Answer =',num_1*num_2)
elif operator=='/':
    print('Answer =',num_1/num_2 .__round__(4))
else:
    print('invalid choice :')
input()