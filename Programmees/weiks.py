hours=int(input('Enter the number of hours :'))
months=hours//720
print(f'In {hours} hours month is : {months}')
weeks=hours//168
print(f'In {hours} hours week is : {weeks}')
days=hours//24
print(f'Number of days in {hours} hours is {days} :')
hour = hours%24
print(f'Left Hours is {hour}')
input()