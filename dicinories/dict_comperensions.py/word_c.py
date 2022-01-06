name=input('Enter a name :')
name_2={i:name.count(i) for i in name}
print(name_2)
for k,v in name_2.items():
    print(k,'in strings is',v,'times:')
input()