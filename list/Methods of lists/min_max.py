numbers=[1,22,33,455,77,88,66,-8]
print(min(numbers))
print(max(numbers))
def gretest(l):
    return max(l)-min(l)
user=int(input('How many entery enter in list :\n'))
print('Enter',user,'entery :')
total=[]
for i in range(user):
    n=int(input())
    total.append(n)
print('maximum value subtract with minimum value :\n')
print(gretest(total))
input()