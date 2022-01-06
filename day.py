print('\t\t\tWEEK DAYS :')
while True:
    user=int(input('Enter  the number between 1 to 7 :'))
    if user<=0 or user >=8:
        print('invalid choice :') 
    elif  user ==1:
        print('THE FIRST DAY OF WEEK IS MONDAY :')
    elif user==2:
        print('THE SECOND DAY OF WEEK IS TUESDAY:')
    elif user==3:
        print('THE THIRD DAY OF WEEK IS WEDNESDAY:')
    elif user==4:
        print('THE FORTH DAY OF WEEK IS THURSDAY:')
    elif user==5:
        print('THE FIVTH DAY OF WEEK IS FRIDAY:')
    elif user==6:
        print('THE SIXTH DAY OF WEEK IS SATURDAY:')
    elif user==7:
        print('THE SEVENTH DAY OF WEEK IS SUNDAY:')
    else:
        pass


input()