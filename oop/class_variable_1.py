class Person:
    msg='Hi there!!'
    def __init__(self,name):
        self.name=name
    def info(self):
        return f"{self.msg}\n{self.name}"
name=input('Enter the name :')
p1=Person(name)
msg_1=input('Enter the message :')
p1.msg=msg_1
print(p1.info())
input()