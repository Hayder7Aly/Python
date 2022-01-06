def dict_1(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,'\t',v)
user=int(input('How many entery enter in dict:'))
print('Enter',user,'Entery :')
total={}
for i in range(1,user+1):
    key=input('Enter the key of dict :')
    value=input('Enter the value of key :')
    total[key]=value
dict_1(**total)
input()
