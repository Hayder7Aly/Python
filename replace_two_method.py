# string='my name is haider and last name is ali'
# print(string.replace(' ','_'))
# print(string.replace('is','was'))
string=input('Enter a string :')
char=input('which char you want to replace :')
char_two=input('that character you want to come in string :')
name=string.replace(char,char_two)
print('new string is :',name)
input()