name=input('Enter your name:')
length=len(name)
print('length of your name is:',length)
char=input('which character you want to count :')
name_two=name.upper().count(char.upper())
print('this character',char,'repeats in',name_two,'times :')
input()

