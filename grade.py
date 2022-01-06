marks=float(input('Enter your marks between 1 to 100 :'))
if marks<0:
    print('invalid choice :')
elif marks==0:
    print('you are failed :')
elif  0<marks<=33:
    print('you are failed :')
elif   33<marks<=50:
    print('your grade is:  C')
elif   50<marks<=60:
    print('your grade is : B')
elif   60<marks<=70:
    print('your grade is : B+')
elif  70<marks<=80:
    print('your grade is : A')
elif  80<marks<=100:
    print('your grade is : A+')
else:
    print('please enter a number between 1 to 100 :')
    input()