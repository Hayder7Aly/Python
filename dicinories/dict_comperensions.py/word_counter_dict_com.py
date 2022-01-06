def counter(d):
    return{char:d.count(char) for char in d}
name=input('Enter any string for count each element in string:')
print(counter(name))
input()
