with open('iofile3.txt','r+') as r:
    data=input('Which data enter in file :')
    r.seek(len(r.read()))
    r.write(f'{data}\n')
input()