from csv import DictWriter
with open('csv_files_writer.csv','w',newline='') as f:
    csv_writer=DictWriter(f,fieldnames=['first_name','last_name','age'])
    csv_writer.writeheader()
    csv_writer.writerow({
        'first_name':'Haider',
        'last_name':'Ali Jutt',
        'age':15
    })
    csv_writer.writerows([
        {'first_name':'Hai','last_name':'Ali jutt','age':15}
    ])
input()