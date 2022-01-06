with open('123.txt','a') as rf:
    rf.write(f'Your style is added :\n')
    row=int(input('Enter a number :'))
    total=''
    for i in range(1,row+1):
        total+=str(i)
        rf.write(f"{total}\n")
