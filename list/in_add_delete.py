user=int(input('How many entery enter in list 1 :'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
list1=total
user2=int(input('How many entery enter in list 2 :'))
print('Enter',user2,'entery :')
total2=[]
for i in range(user2):
    name2=input()
    total2.append(name2)
print(total2)
list2=total2
list1.extend(list2)
print('concatinate of list :')
print(list1)
lsit3=list1
user3=int(input('How many char insert in list :'))
total_1=lsit3
print('Enter',user3,'entery :')
for i in range(user3):
    v=int(input('Enter char in index point :'))
    v2=input('Enter char in string  :')
    total_1.insert(v,v2)
print(total_1)
list4=total_1

char=int(input('How many char delete in list :'))
total3=list4
for i in range(char):
    name=input()
    total3.remove(name)
print(total3)    
input()


