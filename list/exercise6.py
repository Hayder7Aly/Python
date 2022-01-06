def list1(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count

user=[1,2,[3,4],[5,6],[8,9]]
print(list1(user))
input()