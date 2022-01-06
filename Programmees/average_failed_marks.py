students=int(input('How many students marks enter in programme :'))
print('\n\t\t\tEnter',students,'students marks :')
print('\t\t\tEnter marks range 0 to 100 :')
failed_students=0
pass_students=0
possitonal_students=0
average_students_marks=0
for i in range(students):
    marks=int(input())
    average_students_marks+=marks
    if marks<=33 and marks>=0:
        failed_students+=1
    if marks>33:
        pass_students+=1
    if marks>=90 and marks<=100:
        possitonal_students+=1
    else:
        pass 
print('\t\tThe total students whose attempt test -----:',students)
print('\t\tThe students whose pass the test-----------:',pass_students)
print('\t\tThe students whose get 90% marks in test---:',possitonal_students)
print('\t\tThe students whose failed in test is ------:',failed_students)
average=(average_students_marks/students).__round__(2)
print('\t\tThe average of students in test is-------- :',average)
input()