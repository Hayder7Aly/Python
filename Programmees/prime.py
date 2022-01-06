num=int(input('Enter a number :'))
for i in range(2,num+2):
    if num%2!=0 or num==i:
        print(num,'is a prime numbers :')
        break
    else:
        print(num,'is not prime numbers :')
        break
input()
