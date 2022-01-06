for i in range(1):
    name=input('Enter your name :')
    print('Hello ',name,'and Your name is :',name)
    age=int(input('Enter your age :'))
    print('Your age is :',age)
    job=input('Enter your job in factory :')
    print(name,'Your job is :',job)
    times=int(input('How many years you can job in this factory :'))
    if times>=5:
        print(name,'you are senior in this factory :')
    else:
        print(name,'you are junior in this factory :')
    salary=int(input('Enter your salary in this factory :'))
    if salary>=50000:
        print('Your salary get each month bonus and your total salary is :',salary+10000)
    else:
        print('Your salary not get salary :')
    print('Your salary in one Year is :'salary*12)