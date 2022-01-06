user=int(input('How many numbers enter in programmes :'))
total_1=0
total_2=0
print('Enter',user,'entery :')
for i in range(user):
    num=int(input('Enter poositive and negative numbers :'))
    if num>=0:
        total_1+=num
    if num<0:
        total_2+=num
print('\nAddition of possitive numbers is :',total_1)
print('\nSubdtraction of negative numbers is :',total_2)
input()