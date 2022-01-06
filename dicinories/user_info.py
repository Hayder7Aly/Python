name=input("Enter your name :")
age=int(input('Enter your age :'))
roll_no=int(input('Enter your roll_no :'))
clase=input('Enter your class name :')
user_info={
    'name':name,
    'age':age,
    'roll_no':roll_no,
    'clase':clase,
}
print(user_info)
char=input('Which char name print in string :')
print(user_info[char])
input()