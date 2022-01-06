number=int(input('Enter the so on number :'))
print('INTEGERS\tSUM')
total_1=''
total_2=0
for i in range(1,number+1):
    total_1+=str(i)
    total_2+=i
    print(total_1,'\t\t',total_2)
input()