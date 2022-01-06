class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
        return f"\tYOUR FULL NAME IS {self.first_name} {self.last_name} AND YOUR AGE IS {self.age} HAVE A NICE DAY :"
    def age_above(self):
        print('IF AGE GREATER THAN 15 PRINT TRUE ELSE FALSE :')
        return self.age>=15
        
first_name=input('ENTER YOUR FIRST NAME :')
last_name=input('ENTER YOUR LAST NAME:')
age=int(input('ENTER YOUR AGE :'))
p1=Person(first_name,last_name,age)
print(p1.full_name())
print(p1.age_above())
input()