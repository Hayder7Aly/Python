start=int(input('Which char to start print list :'))
stop=int(input('Which char to stop print list :'))
print(list(range(start,stop+1)))
char=int(input('Which char delete in list :'))
char.pop(char)
print(char)
print('Which char delete you in list :')