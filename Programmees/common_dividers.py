print('THIS PROGRAMME FOR COMMON DIVIDERS IN 2 NUMBERS :')
num=int(input('Enter the 1st number :'))
num2=int(input('Enter the 2nd number :'))
total=[]
for i in range(2,num+1):
    if num%i==0 and num2%i==0:
        total.append(i)
for u in total:
    print(u)
input()