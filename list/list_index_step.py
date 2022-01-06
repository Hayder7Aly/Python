name=input('Enter 1st name :')
name2=input('Enter 2nd name :')
name3=input('Enter 3rd name :')
name4=[name,name2,name3]
char=int(input('Which char to start print :'))
char2=int(input('which char to stop print and +1  :'))
char3=int(input('Enter step arrgument :'))
print(name4[char:char2:char3])
input()