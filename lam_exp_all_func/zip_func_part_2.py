l1=[1,3,5,7]
l2=[2,4,6,8]
print(list(zip(l1,l2)))
total=[]
for pair in zip(l1,l2):
    total.append(max(pair))
print(total)
input()