user=int(input('Enter a number  in dict :'))
total={}
for i in range(1,user+1):
    key=i
    value=i*i*i
    total[key]=value
print('Cube values in dict :')
print(total)
input()
