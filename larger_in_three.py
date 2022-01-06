num=float(input('Enter 1st number:'))
num2=float(input('Enter 2nd number :'))
num3=float(input('Enter 3rd number :'))
if num>num2>num3 or num>num3>num2:
    print('Greater number is :',num)
elif num2>num3>num or num2>num>num3 :
    print('Greater number is :',num2)
elif num3>num>num2 or num3>num2>num :
    print('Greater number is :',num3)
input()

