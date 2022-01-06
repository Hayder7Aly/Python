number_1=[1,3,5,7,9,12]
number_2=[2,4,6,8,10]
print(all([i%2==0 for i in number_2])) #---->all function collect all element true:
print(any([i%2==0 for i in number_1])) #---->but any function collect any one element in true :
input()