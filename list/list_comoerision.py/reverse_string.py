user=int(input('How many Entery enter in list :'))
print('Enter',user,'Entery :')
total=[]
for i in range(user):
    string=input()
    total.append(string)
print(total[::-1])
print('Your string all enteries are reversed :')
list_1=[i[::-1] for i in total]
print(list_1)
input()