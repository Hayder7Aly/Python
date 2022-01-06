def key_value(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,'  :  ',v)
user=int(input('How many name enter in dict :'))
print('Enter',user,'name:')
total={}
for i in range(user):
    name=input('Enter the key of dict :')
    name2=input('Enter the value of key :')
    total[name]=name2
key_value(**total)
input()