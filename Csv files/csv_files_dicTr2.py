from csv import DictReader
with open('csv_files_dicTr2.csv','r')as f:
    rank=input('Enter rank and check school ranking !')
    files=DictReader(f)
    for row in files:
        print(row[rank])
print('Ranking of first 5 school in chowk azam:')