with open('data.txt','r+') as r:
    data=input('Enter your name :')
    r.seek(len(r.read()))
    r.write(data)
input()
