user=int(input('How many student height enter in list :'))
print('Enter',user,'student height :')
total=0
total_1=0
total_2=0
for i in range(user):
    height=int(input())
    if height>=155 and height<=165:
        total+=1
    elif height>=0 and height<155:
        total_1+=1
    elif height>165:
        total_2+=1
print('All the student in your school whose height is between 155cm to 165 cm:',total) 
print('All the student in your school whose height is less than 155cm :',total_1)
print('All the student in your school whose height is greater than 165cm : ',total_2)
input()