squares=[2,3,4,5]
print(list(map(lambda a:a**2,squares)))
def num(l):
    return[i**2 for i in l]
print(num(squares))
total=[]
for i in squares:
    total.append(i**2)
print(total)
names=['haider','ali','jutt']
lenght=list(map(len, names))
print(lenght)
input()
