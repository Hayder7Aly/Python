table_number=int(input('Enter a number of table :'))
table_range=int(input('Enter a number for table :'))
for i in range(1,table_range+1):
    print(table_number,' * ',i,' = ',table_number*i)
input()