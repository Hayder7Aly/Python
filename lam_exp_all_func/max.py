user=int(input('HOW MANY NAME AND AGES ENTER IN DICTIONARY :'))
print('ENTER ',user,' NAME AND AGES :')
total={}
for i in range(user):
    name=input('Enter the name:')
    age=int(input('Enter the age :'))
    total[name]=age
print(max(total,key=lambda item:len(item)))