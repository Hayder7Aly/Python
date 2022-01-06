num=int(input('Enter a guess number b/w 1 to 100 :'))
number=54
if num==number:
    print('you win !!!')
elif num>number:
    print('your number is too high :')
else:
    print('your number is too low :')
    input()
