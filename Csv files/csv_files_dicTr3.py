from csv import DictReader
with open('csv_files_dicTr3.csv','r') as f:
    files=DictReader(f)
    user=input('Enter variable for fruits/vegetables:')
    for row in files:
        print(row[user])
input()