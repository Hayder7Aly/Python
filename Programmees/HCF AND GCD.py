num=int(input('Enter the 1st number :'))
num_2=int(input('Enter the 2nd number :'))
total=[]
for i in range(1,num+1):
    if num%i==0 and num_2%i==0:
        total.append(i)
print(total[-1])
input()