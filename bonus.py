user=int(input('How many inputs in name and salary you want :'))
for i in range(1,user+1):
    nam=input('Enter  name :')
    name=nam.upper()
    salary=int(input('Enter  salary :'))
    if salary<=0:
        print('Invalid choice :')
    elif 20000<=salary<=100000:
        print(name,' Your salary get Rs. 5000 bonus  :',salary+5000)
    elif salary>100000:
        print(name,'Your salary get Rs. 15000 bonus  :',salary+15000)
    else:
        print(name,'Your salary not get bonus  Rs.:',salary)   

input()        