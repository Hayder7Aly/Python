print('======Exponent series====== :')
print('x2 +2x2 +3x2......')
user=int(input('Enter a number in series of exponent  :'))
print('Enter' ,user, 'number')
total=0
for i in range(1,user+1):
    total+=i*i
print(total)
input()