class Add:
    def __init__(self,num,num2):
        self.num=num
        self.num2=num2
    def addition(self):
        return f"The addition of two numbers is :{self.num+self.num2}"
p2=Add(4,4)
print(p2.addition())
input()