class Add:
    def __init__(self,num,num2,num3):
        self.num=num
        self.num2=num2
    def total(self):
        return f"Sum of {self.num} and {self.num2} is {self.num+self.num2}"
p1=Add(42,2,'haider')
print(p1.total())
input()