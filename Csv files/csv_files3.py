from csv import reader
with open('csv_files3.csv','r') as f:
    files=reader(f)
    for row in files:
        print(row)
input()