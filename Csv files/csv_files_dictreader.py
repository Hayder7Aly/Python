from csv import DictReader
with open('csv_files_dictreader.csv','r') as f:
    files=DictReader(f,delimiter='|')
    for row in files:
        print(row['name'])
input()