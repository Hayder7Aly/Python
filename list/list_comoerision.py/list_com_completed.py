user_1=int(input('How many int(number) enter in 1st list  :'))
print('Enter',user_1,'Int(number) :')
total_1=[]
for i in range(user_1):
    nums_1=int(input())
    total_1.append(nums_1)
print(total_1)
user_2=int(input('How many float(number) enter in 2nd list :'))
print('Enter',user_2,'float(Number)')
total_2=[]
for i in range(user_2):
    nums_2=float(input())
    total_2.append(nums_2)
print(total_2)
total_1.extend(total_2)
print(total_1)
print('all enter in string foarm :')
lsit_1=[str(i) for i in total_1]
print(lsit_1)
input()