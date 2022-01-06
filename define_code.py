# def add(a,b,c,d,e):
#     return a+b+c+d+e
# def average(a,b,c,d,e):
#     return (a+b+c+d+e)/5 
# def percetage(a,b,c,d,e):
#     return (a+b+c+d+e)*100/500
print('Enter 5 books marks :')
total=0
for i in range(1,6):
    n=float(input())
    total+=n
print('total marks is :',total)
print('average is :',total/5)
print('percentage is :',total*100/500 )
input()
