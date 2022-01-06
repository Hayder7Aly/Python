with open('user_info.txt','r+') as a:
    name=input('Enter your name :')
    rollno=int(input('Enter your age :'))
    email=input('Enter your email :')
    a.seek(len(a.read()))
    a.write(f'\nyour name is :{name}\nyour roll number is :{rollno}\nyour email is :{email}\n')
  
