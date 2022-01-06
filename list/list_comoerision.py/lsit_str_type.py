def nums_list(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]
print(nums_list([1,23,[34,'haider'],'ali','3',1.2]))
nums_list=[1,2,3,[2,34],True,False,4.3]
nums_list_2=[str(i) for i in nums_list if(type(i)==int or type(i)==float)]
print(nums_list_2)
input()