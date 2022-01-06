def user_info(first_name='unknown',last_name='unknown',age='Unknown'):
    if first_name=='':
        first_name='unknown'
    print('your first name is :',first_name)
    if last_name=='':
        last_name='unknown'
    print('your last name is :',last_name)
    if age=='':
        age='unknown'
    print('your age is :',age)
fname=input('Enter your first name :')
lname=input('Enter your last name :')
age_1=input('Enter your age :')
user_info(fname,lname,age_1)
input()
