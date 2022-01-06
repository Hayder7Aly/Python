##  add and delete data :
user_info={
    'name':'haider',
    'last name':'ali', 
    'age':24,
}
print(user_info)
user_info['full name']='haider ali'
print(user_info)
# is used for add data in dicinory:
print(user_info.pop('last name'))
print(user_info)
# is used for delete data from dict :
print(user_info.popitem())
print(user_info)
# is used for delete key and value print in tuple :
input()