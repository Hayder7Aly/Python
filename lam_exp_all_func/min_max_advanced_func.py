names=['haider 007','ali','jutt']
print(max(names,key=lambda item:len(item)))
student=[
    {'name':'Haider','height':154,'age':15},
    {'name':'Ali','height':157,'age':18},
    {'name':'Jutt','height':155,'age':17}
]
print(max(student,key=lambda item:item.get('height'))['name'])
student_1={
    'Haider':{'score':90,'age':15},
    'Ali':{'score':56,'age':19}
}
print(max(student_1,key=lambda item:student_1[item]['score']))
input()