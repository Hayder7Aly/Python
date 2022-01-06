def add(a):
    return a
def factorial(a):
    return a 
User=int(input('Enter a number so one :'))
total=1
total1=[]
total2=0
i=1
while i <=User:
    total1.append(i)
    total2+=i
    total*=i
    i+=1
print('\nThe backward counting of ',User,' is :')
print(total1)
print('\nThe addition of ',User,'all backward  numbers is : ',add(total2))
print('\nThe factorial of ',User,'is : ',factorial(total))
i=0
total3=[]
while i <=User:
    total3.append(i)
    i+=2
print('\nAll even number in ',User,'is : ')
print(total3)  
i=1
total4=[]
while i <=User:
    total4.append(i)
    i+=2
print('\nAll odd number in ',User,' is :')
print(total4) 
print('The square of ',User,'is :',User*User,'\n')
print('The cube of ',User,'is :',User*User*User,'\n')
print('\nThe table of ',User,'is :\n')
i=1
while i <=10:
    print(User,' * ',i,' = ',User*i)
    i+=1
input()