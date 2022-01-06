name=input('Enter your name :')
age=int(input('Enter your age :'))
roll_no=input('Enter your roll_no :')
user_info={
    'name':name,
    'age':age,
    'roll_no':roll_no,
}  
char=input('Which key char found :')
if char in user_info:
    print('present :')
input()