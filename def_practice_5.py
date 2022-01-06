def celcius(a):
    return (a*(9/5)+32).__round__(4) 
def farhienhiet(b):
    return ((b-32)*5/9).__round__(4)
C=float(input('Enter celcius scale :'))
F=float(input('Enter farhienhiet scale:'))
print('celcius scale in farhienhiet scale :',celcius(C))
print('farhienhiet scale in celcius scale :',farhienhiet(F))
input()