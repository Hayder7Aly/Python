n=input('Enter 1st name :')
n2=input('Enter 2nd name :')
n3=input('Enter 3rd name :')
n4={
    'name1':n,
    'name2':n2,
    'name3':n3,
}
print(n4)
char=input('Which key delete in dicinory :')
print(n4.pop(char))
print(n4)
input()