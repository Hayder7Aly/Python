user=int(input('Enter the number of range :'))
even_expo=int(input('Enter the number which apply all even number :'))
odd_expo=int(input('Enter the number which apply all odd number :'))
comp={i**even_expo if i%2==0 else i**odd_expo for i in range(1,user+1)}
print(comp.union())
input()
