from csv import DictWriter
with open('csv_files_writer3.csv','w',newline='')as f:
    csv_writer=DictWriter(f,fieldnames=['name','age','class'])
    csv_writer.writeheader()
    name=input('Enter your name :')
    age=input('Enter your age :')
    nclass=input('Enter your class :')
    csv_writer.writerow({
         'name':name,
         'age':age,
         'class':nclass
    })
input()