def odd_even(num,num2,*args):
    return[i*num if i%2==0 else i*num2 for i in args]
range_1=int(input('Enter the range of number :'))
num_1=range(1,range_1+1)
expo_1=int(input('Enter the number multiply on even number :'))
expo_2=int(input('Enter the number multiply on odd number :'))
print(odd_even(expo_1,expo_2,*num_1))
input()