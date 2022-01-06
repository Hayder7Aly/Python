user=int(input('HOW MANY STUDENTS MARKS ENTER IN LIST :'))
print('ENTER',user,'STUDENTS MARKS :')
total=[]
for i in range(user):
    marks=int(input('Enter the student marks :'))
    total.append(marks)
print('\t\tLOWEST MARKS IN TEST IS :',min(total))
print('\t\tGREATEST MARKS IN TEST IS :',max(total))
input()