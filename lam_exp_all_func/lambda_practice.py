func=lambda number:True if number%2==0 else False
print(func(4+1)) 
func_2=lambda string: string if len(string)>5 else 'nanana'
print(func_2('hai'))
func_3=lambda s:s[::-1]
print(func_3('haider'))
input()