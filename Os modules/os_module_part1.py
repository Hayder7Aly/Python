import os
print(os.getcwd())
movie=input('Enter a movie name for folder:')
if os.path.exists(movie):
    print('Already exits :')
else:
    os.mkdir(movie)
input()