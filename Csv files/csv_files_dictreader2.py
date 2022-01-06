from csv import DictReader
with open('csv_files_dictreader2.csv','r') as f:
    files=DictReader(f)
    user=input('Enter a char in csv files you want :')
    for i in files:
        print(i[user])
input()