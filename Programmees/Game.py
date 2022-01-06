print('\t\t\t===Number guessing game===\n\n\n ')
guess=int(input('How many times you want to guess a number : '))
import random
winning_number=random.randint(1,100)
i=0
while i<=guess:
    if i==guess:
        print('\n\t\tGame over :')
        print('\n\n\t\tThe winning_number is :',winning_number)
        break
    user_guess=int(input('Enter a number between 1 to 100:  '))
    if user_guess==winning_number:
        print('You win !!!, and you just guess ',i+1,'times : ')
        break
    elif user_guess>winning_number:
        print('Too High :')
    elif user_guess<winning_number:
        print('Too Low :')
    i+=1
input()    

