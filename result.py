n1=int(input('Enter your marks in Math :'))
if n1 <=33:
    print('You are failed in Math subject :')
n2=int(input('Enter your marks in Science :'))
if n2<=33:
    print('You are failed in Science subject :')
n3=int(input('Enter your marks in Urdu subject :'))
if n3<=33:
    print('You are failed in Urdu subject :')
n4=int(input('Enter your marks in Islamiyat :'))
if  n4 <=33:
    print('You are failed in Islamiyat subject :')
n5=int(input('Enter your marks in English :'))
if  n5 <=33:
    print('You are failed in English subject :')
n6=int(input('Enter your marks in Pak-Study :'))
if  n6 <=33:
    print('You are failed in Pak-Study subject :')
n7=n1+n2+n3+n4+n5+n6
print('Total number is 600 And obtain marks is    :', n7)
n8=n7/6
print('Average of :', n7, '  is    :',n8.__round__(4))
n9=(n7/600)*100
print('Percentage of  :',n7,'is     :',n9.__round__(4),'%')
if n7 <=250:
    print('You are failed :',n7)
else:
    print('Congratulation you have passed :')

input()


