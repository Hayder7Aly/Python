from csv import DictWriter
with open('csv_writer2.csv','w',newline="") as f:
    files=DictWriter(f,fieldnames=['name','rollno'])
    files.writeheader()
    user=int(input('Enter a number who many students name enter in programme:'))
    for i in range(user):
        name=input('Enter your name :')
        rn=input('Enter your Roll Number :')
        files.writerow({
            'name':name,
            'rollno':rn
        }
        )
# from csv import DictWriter
# with open('writer.csv','w',newline='')as f:
#     files=DictWriter(f,fieldnames=['name'])
#     files.writeheader()
#     files.writerows([
#         {'name':'haider'},
#         {'name':'ali'}
#     ])