class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
p1=Person('haider',15,154)
print(f"HELLO {p1.name} .")
print(f'YOUR AGE IS {p1.age} .')
print(f'YOUR HEIGHT IS {p1.height} CM .')
input()