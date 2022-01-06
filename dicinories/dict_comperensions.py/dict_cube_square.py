num=int(input('Enter the so on number :'))
exponent=int(input('Enter the exponent number which apply all vlaues:'))
dict_1={i:i**exponent for i in range(1,num+1)}
print(dict_1)
for k,v in dict_1.items():
    print(k,'exponent is',exponent,'and answer is',v)
input()