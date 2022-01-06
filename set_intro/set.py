## set is data type :
## unordered collection of unique items :
## we store just int/float and string :
s={1,2,3,'hader'}
print(s)
s1=list(set([1,2,3,4,5,6,7,8,9,1,2,3,4,5]))
print(s1)
## add ,remove,copy,clear,discard data :
ss={1,2,3,4,'haider',12,3}
ss.add(4)
ss.add(76)
print(ss)
ss.remove(4)
ss.discard(56)
print(ss)
ss.copy()
print(ss)
ss.clear()
print(ss)
input()