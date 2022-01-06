table_number=int(input('Enter the number of table :'))
table_range=int(input('Enter the number for table :'))
for i in range(1,table_range+1):
    print(table_number,' * ',table_range,' = ',table_number*table_range)
    table_range=table_range-1
input()