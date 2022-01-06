print('guess a number for close the programme :')
print('\n between 1 to 10 :')
import random
w_n=random.randint(1,10)
while True:
    user=int(input('Enter a number :'))
    if user==w_n:
        print('Congratulation you have close the programme :')
        break
    if user!=w_n:
        print('guess again :')
input()
    