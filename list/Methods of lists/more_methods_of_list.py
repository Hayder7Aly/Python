numbers2=list(range(1,11))
numbers=[1,2,3,4,5,6,7,1,2,3,4,5,1,5,1,6,1,7,6,4,1,1]
print(numbers)
# range is used for ask list items :
# list is used for ask list generate :
print(numbers.pop(2))
# pop is used for delete char in list but its returns the delete items in print:
print(numbers.index(1))
#is used for index in list items index point :
print(numbers.index(1,3))
# 2nd argument is used for check items after 2nd argument index ;
# print(numbers.index(1,7,11))
#is used for 3rd argument stop index point in numbers :
def negative_number(a):
    negative=[]
    for i in a:
        negative.append(-i)
    return negative
print(negative_number(numbers2))
#is used for negative lsit in for loop :
input()



