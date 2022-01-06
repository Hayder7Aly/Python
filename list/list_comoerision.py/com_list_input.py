user=int(input('How many number enter in list :'))
print('Enter',user,'Entery :')
char=int(input('Enter the number of exponent for all list enteries :'))
list_1=[i**char for i in range(1,user+1)]
print(list_1)
input()
