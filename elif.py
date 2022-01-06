age=int(input('Enter your age :'))
if age <=0:
    print('Invalid choise :')
elif 0<age<=3:
    print("Ticket price free :")
elif 3<age<=25:
    print('ticket price : Rs. 350')
elif 25<age<40:
    print('ticket price : Rs. 400')
elif 40<age<=60:
    print('ticket price : Rs. 500')
else: 
    print('ticket price : Rs. 700 ')
    input()