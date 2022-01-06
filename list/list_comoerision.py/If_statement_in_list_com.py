user=int(input('Enter so on numbers :'))
total=[]
for i in range(user+1):
    total.append(i)
print(total)
list_1=[i for i in range(user+1) if i%2==0]
list_2=[i for i in range(user+1) if i%2!=0] 
print('EVEN NUMBER LIST in:',user)
print(list_1)
print('ODD NUMBER LIST  in:',user)
print(list_2)
input()