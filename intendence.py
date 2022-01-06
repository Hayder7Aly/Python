user=int(input('Enter how many students names enter in directory  :'))
print('Enter',user,'names :')
# print('And their roll no :')
total=[]
for i in range(user):
    name=input()
    total.append(name)
print(total)
print('\n'.join(total))
char=input('Which character you find in dirictory :')
for i in total:
    if i in char :
        print(i)
        print('Present :')
input()
  


