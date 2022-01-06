def greatest(a,b,c):
    if a>b>c or a>c>b :
        return a
    elif b>c>a or b>a>c :
        return b
    elif c>a>b or c>b>a:
        return c
    else:
        if a==b==c:
            pass
n=float(input('enter 1st number :'))
n2=float(input('enter 2nd number :'))
n3=float(input('enter 3rd number :'))
total=greatest(n,n2,n3)
print(total,'greater number is :')
input()