def generator_func(n):
    for i in range(1,n+1):
        if i%2==0:
            yield(i)
number=int(input('Enter the number :'))
for number in generator_func(number):
    print(number)
# BUT WE CAN STORE GENERATOR FUNC IN VARIABLE AND CANN'T USE DOUBLE LOOP
input()