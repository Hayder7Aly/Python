def odd_even(**kwargs):
    return{i:i**2 for k,v in kwargs.items() if i%2==0  }
user=int(input('Enter the number :'))
total={}
for i in range(1,user+1):
    string=str(i)
    values=i
    total[string]=i
print(odd_even(**total))
input()