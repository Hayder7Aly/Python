square={num:num**2 for num in range(1,11)}
print(square)
for k,v in square.items():
    print('Square of',k,'is',v)
string='haider ali'
count={char:string.count(char) for char in string}
print(count)
for k,v in count.items():
    print(k,'in string is',v)
input()