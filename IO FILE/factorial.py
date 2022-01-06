with open('factorial.txt','r+') as r:
    n=int(input('Enter a number :'))
    total=1
    for i in range(1,n+1):
        total=total*i
    r.seek(len(r.read()))
    r.write(f'factorial of {n} = {total}\n')