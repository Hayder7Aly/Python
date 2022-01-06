names=['haider','ali','jutt']
for pos,name in enumerate(names):
    print(pos,'------->',name)
def n_p(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos,'--------->',name
    return 'not found'
lsist=['haider','ali','jutt']
print(n_p(lsist,'haider'))
input()