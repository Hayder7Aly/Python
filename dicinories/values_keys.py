name=input('Enter your name :')
age=int(input('Enter your age :'))
roll_no=input('Enter your roll_no :')
user_info={
    'name':name,
    'age':age,
    'roll_no':roll_no,
}  
print(user_info)
for i,j in user_info.items():
    print(i," : ",j)
input()
