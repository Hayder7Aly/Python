print('\n\n\n\t\t\t======>HOTTEL MANAGEMENT<======')
name=input('\t\t\nEnter your name :')
room=input('\n\tEnter your room number and its name :')
stay=int(input('\n\tEnter your stay in hottel how many days :'))
clase=input('\n\tEnter your class in hottle :')
if 0>=stay>=32:
    print('\n\tInvalid choice :')
elif 0<stay<=10:
    print('\n\tYour bill of hottel is Rs.',stay*6000)
elif 10<stay<=15:
    print('\n\tYour bill of hottel is Rs.',stay*9000)
elif 15<stay<=25:
    print('\n\tYour bill of hottel is Rs.',stay*15000)
elif 25<stay<=30:
    print('\n\tYour bill of hottel is Rs.',stay*18000)
elif 30<stay<=31:
    print('\n\tYou spent one month in this hottel :')
    print('\n\tYou get discount in hottel one day stayment :')
    print('\n\tyour bill is Rs.',(stay-1)*18000)
input()
