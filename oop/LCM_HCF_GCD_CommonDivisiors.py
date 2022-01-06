num=int(input('Enter the 1st number :'))
num2=int(input('Enter the 2nd number :'))
total=[]
for i in range(2,num+1):
    if num%i==0 and num2%i==0:
        total.append(i)
print('ALL COMMON DIVISIORS IN TWO NUMBER IS :')
for i in total:
    print(i)
for i in total:
    print('LCM of two number is :',i)
    break
total1=total[::-1]
for i in total1:
    print('HCF\GCD  of two number si :',i)
    break
input()