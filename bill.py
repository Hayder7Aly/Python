print('\n\n\t\t================>BILLING<===============\n\n')
unit=int(input('\tEnter Unit consumed in this month :'))
if unit<=0:
    print('\nInvalid choice :')
elif 0<unit<=100:
    print('\n\tYour Bill is Rs.',unit*9)
elif 100<unit<=200:
    print('\n\tYour Bill is Rs.',unit*15)
elif 200<unit<=350:
    print('\n\tYour Bill is Rs.',unit*20)
elif 350<unit<=500:
    print('\n\tYour Bill is Rs.',unit*25)
else:
    print('Your Bill pay tax Rs.5000')
    print('Your Bill is Rs.',unit*35+5000)
input()
