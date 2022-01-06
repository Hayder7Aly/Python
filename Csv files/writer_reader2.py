from csv import DictReader,DictWriter
with open('writer_readerpart1.csv','r')as f:
    with open('writer_readerpart2.csv','w',newline='')as w:
        files=DictReader(f)
        files2=DictWriter(w,fieldnames=['name','age'])
        files2.writeheader()
        for row in files:
            name,age=row['name'],row['age']
            files2.writerow({
                'name':name,
                'age':age
            })