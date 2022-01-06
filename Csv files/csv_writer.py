from csv import DictWriter
with open('csv_writer.csv','w',newline='')as f:
    files=DictWriter(f,fieldnames=['name','age','school'])
    files.writeheader()
    name=input('Enter your name:')
    age=int(input('Enter your age  :'))
    school=input('Enter your school :')
    files.writerow({
        'name':name,
        'age':age,
        'school':school
    }

    )
 