user_info={
    'name':'haider',
    'age':15,
    'fav_movies':['coco','adelia'],
    'fav_tunes ':['aweaking','cycling'],
}
if 'name' in user_info:
    print('present:')
else:
    print('not present:')
for i in user_info.keys():
    print(i)
for i in user_info.values():
    print(i)
for i in user_info.items():
    print(i)
# items  is user for dict in tupple
for i,j in user_info.items():
    print(i,':',j) 
input()  
