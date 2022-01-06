print('Enter at least 5 entery :')
user=int(input('How many entery enter in list :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
list1=total
char=int(input('Enter char delete in list in index :\n'))
list1.pop(char)
print(list1)
char2=int(input('Enter char delete in list in index :\n'))
del list1[char2]
print(list1)
char3=input("Enter char delete in list in string :\n")
list1.remove(char3)
print(list1)
input()
