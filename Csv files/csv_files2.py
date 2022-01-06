from csv import reader
with open('csv_files2.csv','r') as f:
    files=reader(f)
    for row in files:
        print(row)
input()