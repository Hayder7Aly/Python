d=dict.fromkeys(('name','age'),'haider')
print(d)
d2=dict.fromkeys('abc','unknown')
print(d2)
d3=dict.fromkeys(range(1,11),'Haider ali')
print(d3)
d4=dict.fromkeys(['name','age'],['unknown'])
print(d4)
g={'name':'hadier','age':'15'}
print(g.get('name'))
g={'name':'hadier','age':'15'}
if g.get('name'):
    print('true')
else:
    print('false')
g={'name':'hadier','age':'15'}
g.clear()
print(g)
g={'name':'hadier','age':'15'}
g1=g.copy()
print(g)
print(g1)
g={'name':'hadier','age':'15'}
g1=g.copy()
g.popitem()
print(g)
print(g1)
input()
