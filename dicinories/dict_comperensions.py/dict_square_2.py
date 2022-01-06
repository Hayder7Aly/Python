user=int(input('How many number enter in dict :'))
print('Enter',user,'Number:')
total={}
for i in range(user):
    number=int(input())
    total[number]=number**2
print(total)
for k,v in total.items():
    print('Square of',k,'is',v)
input()
    
    