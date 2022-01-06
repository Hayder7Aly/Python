# name='haider'
# if name:
#     print('not empty :')
# else:
#     print('empty :')
name=input('enter your name :')
age=input('enter your age :')
if name and age:
    print('your name is ',name,'and age is ',age)
elif age or name :
    print('you can type just one string :',age,name)
else:
    print("you can't type anything :")
    
input()