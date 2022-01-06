obtain=float(input('Enter your obtain marks  :'))
total=float(input('Enter your total marks :'))
per=obtain*100/total
if per<0:
     print('invalid choice :')
elif per==0:
    print('you are failed :',per,'%')
elif  0<per<=33:
    print('you are failed :',per,'%')
elif   33<per<=50:
    print('your grade is:  C',per,'%')
elif   50<per<=60:
    print('your grade is : B',per,'%')
elif   60<per<=70:
    print('your grade is : B+',per,'%')
elif  70<per<=80:
    print('your grade is : A',per,'%')
else:
    print('your grade is : A+',per,'%')
    input()















