total={}
name=input('Enter your name :')
age=int(input('Enter your age :'))
fav_movies=input('Enter your fav_movies (,)seprated :').split()
fav_tunes=input('Enter your fav_tunes (,)seprated :').split()
total['name']=name
total['age']=age
total['fav_movies']=list(fav_movies)
total['fav_tunes']=list(fav_tunes)
print(total)
for i,j in total.items():
    print(i,':',j)
input()
