class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def info(self):
        if self.height>=155 and self.height<=165:
            print('\tYour height is between 155cm to 165 cm :')
        return f"\tHello {self.name} Your age is {self.age} and your height is {self.height} cm ."
name=input('Enter your name :')
age=int(input('Enter your age :'))
height=int(input('Enter your height in centimeter :'))
p1=Person(name,age,height)
print(p1.info())
input()