num=int(input('Enter a number so on :'))
print('Skip all numbers those divided by 7 :')
for  i in range(1,num+1):
    if i%7!=0:
        print(i)
    else:
        pass
input()