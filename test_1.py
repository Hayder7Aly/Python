print('Enter 10 numbers :')
total=[]
for i in range(10):
    num=input()
    if num.isdigit(): 
        total.append(num)
    else:
        print('invalid input !')
        continue
total_0=total[::-1]
print('All number print in decesending order :')
sum1 =0
for i in total_0:
    print(i)
    sum1 = sum1 + int(i)
print('maxmium number in list :',max(total))
print('minimum number in list :',min(total))
print('sum of all number is :',sum1)
print('average of all number is :',sum1/5)
input()