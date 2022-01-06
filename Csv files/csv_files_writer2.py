from csv import DictWriter
with open('csv_files_writer2.csv','w',newline='') as f:
    csv_writer=DictWriter(f,fieldnames=['name','salary','department'])
    csv_writer.writeheader()
    name=input('Enter your name:')
    salary=int(input('Enter your salary :'))
    department=input('Enter your department :')
    csv_writer.writerow({
        'name':name,
        'salary':salary,
        'department':department
    })