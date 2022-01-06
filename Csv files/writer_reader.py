from csv import DictReader,DictWriter
with open('writer_reader.csv','r')as rf:
    with open('writer_reader2.csv','w',newline='') as wf:
        csv_reader=DictReader(rf)
        csv_writer=DictWriter(wf,fieldnames=['name','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            name,age=row['name'],row['age']
            csv_writer.writerow({
                'name':name,
                'age':age
            })