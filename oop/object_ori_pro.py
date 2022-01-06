class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        return f"Your name is {self.name} and your age is {self.age}"
class Person_two(Person):
    def __init__(self,name,age,roll_no):
        Person.__init__(self,name,age)
        self.roll_no=roll_no
    def info_2(self):
        return f"Your name is {self.name} and age is {self.age} roll_number is {self.roll_no}"
name=input('Enter your name :')
age=int(input('Enter your age :'))
roll_no=int(input('Enter your roll number :'))
p1=Person(name,age)
p2=Person_two(name,age,roll_no)
print(p1.info())
print(p2.info_2())
input()