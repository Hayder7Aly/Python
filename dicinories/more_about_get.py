# d={'name':'haier','age':12}
# print(d.get('name2','not foune!'))
key=input('Enter your 1st key :')
key2=input('Enter your 2nd key :')
value=input('Enter your 1st value :')
d=dict.fromkeys((key,key2),value)
print(d)
input()
